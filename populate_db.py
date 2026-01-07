import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toystore.settings')
django.setup()

from store.models import Category, Product

# Create categories
categories_data = [
    {'name': 'Action Figures', 'slug': 'action-figures'},
    {'name': 'Dolls', 'slug': 'dolls'},
    {'name': 'Educational', 'slug': 'educational'},
    {'name': 'Outdoor', 'slug': 'outdoor'},
]

for cat_data in categories_data:
    Category.objects.get_or_create(**cat_data)

# Create sample products
products_data = [
    {
        'name': 'Super Hero Action Figure',
        'slug': 'super-hero-action-figure',
        'description': 'Amazing superhero action figure with movable joints and accessories. Perfect for imaginative play!',
        'price': 24.99,
        'category': Category.objects.get(slug='action-figures'),
        'in_stock': True,
    },
    {
        'name': 'Princess Doll',
        'slug': 'princess-doll',
        'description': 'Beautiful princess doll with elegant dress and accessories. Great for creative storytelling.',
        'price': 29.99,
        'category': Category.objects.get(slug='dolls'),
        'in_stock': True,
    },
    {
        'name': 'STEM Building Blocks',
        'slug': 'stem-building-blocks',
        'description': 'Educational building blocks that teach engineering and creativity. 200+ pieces included!',
        'price': 39.99,
        'category': Category.objects.get(slug='educational'),
        'in_stock': True,
    },
    {
        'name': 'Flying Disc Set',
        'slug': 'flying-disc-set',
        'description': 'Colorful flying disc set for outdoor fun. Includes 3 discs of different sizes.',
        'price': 14.99,
        'category': Category.objects.get(slug='outdoor'),
        'in_stock': True,
    },
    {
        'name': 'Robot Warrior',
        'slug': 'robot-warrior',
        'description': 'Futuristic robot action figure with light-up features and sound effects.',
        'price': 34.99,
        'category': Category.objects.get(slug='action-figures'),
        'in_stock': True,
    },
    {
        'name': 'Science Lab Kit',
        'slug': 'science-lab-kit',
        'description': 'Complete science lab kit with 50+ experiments. Perfect for young scientists!',
        'price': 49.99,
        'category': Category.objects.get(slug='educational'),
        'in_stock': True,
    },
]

for prod_data in products_data:
    Product.objects.get_or_create(**prod_data)

print("Sample data created successfully!")
print(f"Categories: {Category.objects.count()}")
print(f"Products: {Product.objects.count()}")
