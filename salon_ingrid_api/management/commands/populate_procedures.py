from django.core.management.base import BaseCommand
from salon_ingrid_api.models import Procedure
from datetime import timedelta


class Command(BaseCommand):
    help = 'Fill the Procedure model with predefined data'

    def handle(self, *args, **kwargs):
        # Data extracted from the provided HTML content
        procedures = [
            {"name": "Celkové ošetření obličeje a dekoltu (s masáží)", "duration": timedelta(minutes=90),
             "description": "(ošetření na míru dle potřeb vaší pleti, včetně hloubkového čištění, masáže "
                            "obličeje a dekoltu a parafínového zábalu rukou)"},
            {"name": "Celkové ošetření obličeje a dekoltu (bez masáže)", "duration": timedelta(minutes=60),
             "description": "(ošetření na míru dle potřeb vaší pleti, včetně hloubkového čištění)"},
            {"name": "Teenage ošetření (mladistvá pleť)", "duration": timedelta(minutes=60),
             "description": "(odlíčení, zjemnění pleti, hloubkové čištění, zklidňující maska, závěrečný krém)"},
            {"name": "Lash Lifting + Lash Botox", "duration": timedelta(minutes=60), "description": ""},
            {"name": "Laminace obočí s barvením", "duration": timedelta(minutes=60), "description": ""},
            {"name": "Úprava a barvení obočí (v rámci ošetření pokud již není v ceně/samostatně)",
             "duration": timedelta(minutes=30), "description": ""},
            {"name": "Úprava obočí a barvení - BROW CODE (efekt henny)", "duration": timedelta(minutes=30),
             "description": ""},
            {"name": "Barvení řas (v rámci ošetření/samostatně)", "duration": timedelta(minutes=30),
             "description": ""},
            {"name": "Epilace voskem - Horní ret/brada/oblast pupku", "duration": timedelta(minutes=15),
             "description": ""},
            {"name": "Epilace voskem - Celý obličej", "duration": timedelta(minutes=30), "description": ""},
            {"name": "Epilace voskem - Třísla/podpaží", "duration": timedelta(minutes=30), "description": ""},
            {"name": "Epilace cukrovou pastou - Nohy: po kolena/celé", "duration": timedelta(minutes=60),
             "description": ""},
            {"name": "Epilace cukrovou pastou - Ruce: po loket/celé", "duration": timedelta(minutes=45),
             "description": ""},
            {"name": "Epilace cukrovou pastou - Hrudník", "duration": timedelta(minutes=60), "description": ""},
            {"name": "Epilace cukrovou pastou - Záda", "duration": timedelta(minutes=60), "description": ""},
            {"name": "Denní líčení (po ošetření)", "duration": timedelta(minutes=30), "description": ""},
            {"name": "Večerní/slavnostní líčení", "duration": timedelta(minutes=60), "description": ""},
            {"name": "Svatební líčení (včetně zkoušky)", "duration": timedelta(minutes=120), "description": ""},
            {"name": "Lepení řas v rámci líčení", "duration": timedelta(minutes=30), "description": ""},
            {"name": "Individuální kurz líčení (3,5 - 4 h)", "duration": timedelta(hours=4), "description": ""}
        ]

        for procedure in procedures:
            Procedure.objects.create(
                name=procedure["name"],
                duration=procedure["duration"],
                description=procedure["description"]
            )

        self.stdout.write(self.style.SUCCESS('Procedures have been added successfully.'))