from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    """Home page model."""

    templates = "templates/home/home_page.html" # Specified the template for the homepage
    max_count = 1 # Specifies that only 1 home page is allowed

    banner_title = models.CharField(max_length=100, blank=False, null=True) # Creates a column called banner_title in homepage table

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ] # Makes banner title field editable in the admin panel

    class Meta:

        verbose_name = "Home Page" # Calls the page Home Page (same as default)
        verbose_name_plural = "Home Pages"