from django.db import migrations, models


def seed_portfolio_items(apps, schema_editor):
    PortfolioItem = apps.get_model("appointments", "PortfolioItem")
    PortfolioItem.objects.bulk_create([
        PortfolioItem(
            title="A natural, brighter smile",
            category="Smile design",
            description="A subtle whitening and bonding plan designed around the patient’s natural features.",
            result="A confident smile that still feels like her",
            image_url="https://images.unsplash.com/photo-1606265752439-1f18756aa2fc?auto=format&fit=crop&w=1200&q=85",
            display_order=1,
        ),
        PortfolioItem(
            title="Restored with confidence",
            category="Restorative care",
            description="Comfort-first restorative work that brought back balance, function, and everyday ease.",
            result="Comfort and confidence, rebuilt together",
            image_url="https://images.unsplash.com/photo-1609840114035-3c981b782dfe?auto=format&fit=crop&w=1200&q=85",
            display_order=2,
        ),
        PortfolioItem(
            title="A fresh start for a growing smile",
            category="Family dentistry",
            description="An encouraging first visit that made regular dental care feel simple and approachable.",
            result="A positive routine from the very beginning",
            image_url="https://images.unsplash.com/photo-1588776814546-daab30f310ce?auto=format&fit=crop&w=1200&q=85",
            display_order=3,
        ),
        PortfolioItem(
            title="Small changes, meaningful difference",
            category="Preventive care",
            description="A focused care plan and a few small habit changes helped this patient protect their smile.",
            result="Healthier habits with less worry",
            image_url="https://images.unsplash.com/photo-1550831107-1553da8c8464?auto=format&fit=crop&w=1200&q=85",
            display_order=4,
        ),
    ])


class Migration(migrations.Migration):
    dependencies = [("appointments", "0002_blogpost")]

    operations = [
        migrations.CreateModel(
            name="PortfolioItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("category", models.CharField(max_length=80)),
                ("description", models.TextField()),
                ("result", models.CharField(max_length=180)),
                ("image_url", models.URLField(max_length=500)),
                ("is_featured", models.BooleanField(default=True)),
                ("display_order", models.PositiveSmallIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "title"]},
        ),
        migrations.RunPython(seed_portfolio_items, migrations.RunPython.noop),
    ]
