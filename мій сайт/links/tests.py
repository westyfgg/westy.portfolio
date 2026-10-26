from django.test import TestCase
from django.urls import reverse

from .models import ProfileLink, SiteProfile


class ProfilePageTests(TestCase):
    def test_home_page_shows_profile_quote_and_default_links(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "@WESTY")
        self.assertContains(response, "«Роби з душею — і результат говоритиме сам за себе.»")
        for title in (
            "My Telegram",
            "TikTok",
            "Info",
            "Stars",
            "Telegram Premium",
            "Price",
            "Contact me",
        ):
            self.assertContains(response, title)

    def test_link_urls_are_editable_and_open_safely(self):
        profile = SiteProfile.get_profile()
        link = ProfileLink.objects.get(profile=profile, title="My Telegram")
        link.url = "https://t.me/westy"
        link.save()

        response = self.client.get(reverse("home"))

        self.assertContains(response, 'href="https://t.me/westy"')
        self.assertContains(response, 'rel="noopener noreferrer"')

    def test_inactive_links_are_hidden(self):
        link = ProfileLink.objects.get(title="TikTok")
        link.is_active = False
        link.save()

        response = self.client.get(reverse("home"))

        self.assertNotContains(response, "TikTok")

    def test_admin_is_available(self):
        response = self.client.get("/admin/login/")

        self.assertEqual(response.status_code, 200)
