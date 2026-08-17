from django.db import migrations, models
import django.utils.timezone


def seed_blog_posts(apps, schema_editor):
    BlogPost = apps.get_model("appointments", "BlogPost")
    BlogPost.objects.bulk_create([
        BlogPost(
            title="The two-minute habit that protects your smile",
            slug="two-minute-habit-protects-your-smile",
            category="Everyday care",
            excerpt="Small, consistent habits do more for your long-term oral health than occasional bursts of effort.",
            body="A healthy smile is built in the ordinary moments. Brushing for two full minutes twice a day helps remove plaque before it can harden into tartar.\n\nPair that habit with a soft-bristled brush, fluoride toothpaste, and gentle attention along the gumline. It is a simple routine, but it gives your smile a strong foundation between visits.",
            featured_image="https://images.unsplash.com/photo-1559591937-e5f5d9b9e7d1?auto=format&fit=crop&w=1200&q=85",
            author="Dr. Maya Chen",
            read_time=4,
        ),
        BlogPost(
            title="What to expect at your first visit",
            slug="what-to-expect-first-dental-visit",
            category="Your visit",
            excerpt="A first appointment should feel like a conversation, not a test. Here is how we make it easy.",
            body="Your first visit starts with listening. We will talk about your goals, answer questions, and learn what makes you feel comfortable.\n\nAfter that conversation, we complete a thoughtful exam and share what we see in clear, everyday language. You will leave with options and a plan we build together, never a surprise recommendation.",
            featured_image="https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=1200&q=85",
            author="The Northstar team",
            read_time=5,
        ),
        BlogPost(
            title="A calmer approach to dental anxiety",
            slug="calmer-approach-dental-anxiety",
            category="Comfort",
            excerpt="You are not behind, and you are not alone. These small choices can make dental care feel more manageable.",
            body="Dental anxiety is common, and there is no right way to feel about an appointment. Sharing your concerns before we begin helps us shape the visit around you.\n\nYou can ask for pauses, a step-by-step explanation, or a quieter start. Comfort is not an extra at Northstar; it is part of good care.",
            featured_image="https://images.unsplash.com/photo-1588776814546-daab30f310ce?auto=format&fit=crop&w=1200&q=85",
            author="Dr. Maya Chen",
            read_time=3,
        ),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ("appointments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("category", models.CharField(max_length=80)),
                ("excerpt", models.TextField()),
                ("body", models.TextField()),
                ("featured_image", models.URLField(max_length=500)),
                ("author", models.CharField(default="Northstar Dental team", max_length=120)),
                ("read_time", models.PositiveSmallIntegerField(default=4)),
                ("published_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_published", models.BooleanField(default=True)),
            ],
            options={"ordering": ["-published_at"]},
        ),
        migrations.RunPython(seed_blog_posts, migrations.RunPython.noop),
    ]
