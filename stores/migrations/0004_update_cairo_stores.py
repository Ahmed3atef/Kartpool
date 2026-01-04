from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path
from django.utils import timezone

DATA_FILENAME = 'data/data.json'
CITY = 'Cairo'

def load_data(apps, schema_editor):
    Store = apps.get_model('stores', 'Store')
    # Path is relative to the migration file: stores/migrations/
    # parents[0] = migrations
    # parents[1] = stores
    # parents[2] = Project Root (Kartpool)
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    if not jsonfile.exists():
        print(f"Data file not found: {jsonfile}")
        return

    with open(str(jsonfile), encoding='utf-8') as datafile:
        objects = json.load(datafile)
        elements = objects.get('elements', [])
        
        for obj in elements:
            try:
                objType = obj.get('type')
                if objType == 'node':
                    tags = obj.get('tags', {})
                    # Prioritize 'name', then 'name:en', then 'N/A'
                    name = tags.get('name') or tags.get('name:en') or 'N/A'

                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)

                    housenumber = tags.get('addr:housenumber', 'N/A')
                    street = tags.get('addr:street', 'N/A')
                    postcode = tags.get('addr:postcode', 'N/A')
                    address = f"{housenumber},{street},{postcode}"

                    store_type = tags.get('shop', 'N/A')
                    phone = tags.get('phone', 'N/A')
                    
                    # Prevent duplicates by checking name and coordinates
                    # Using a small tolerance for float comparison could be better but exact match 
                    # is safer against adding the same file content twice.
                    if not Store.objects.filter(
                        name=name, 
                        latitude=latitude, 
                        longitude=longitude
                    ).exists():
                        Store.objects.create(
                            created_at=timezone.now(),
                            name=name,
                            latitude=latitude,
                            longitude=longitude,
                            location=location,
                            store_type=store_type,
                            phone=phone[:100],
                            address=address[:100],
                            city=CITY,
                        )
            except Exception as e:
                # Log error or pass
                pass

class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_remove_store_inventory_store_inventory'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
