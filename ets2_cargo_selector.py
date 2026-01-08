import customtkinter as ctk
import pandas as pd
import tkinter as tk
import re

# --- KONFIGURATION ---
PRI_RED = "#650303"
SEC_WHITE = "#FFFFFF"
ADR_ORANGE = "#FF8C00"

translations_cargo = {
    'cn_acetylene': 'Acetylen', 'cn_acid': 'Säure', 'cn_aircraft_tires': 'Flugzeugreifen',
    'cn_air_mails': 'Luftpost', 'cn_almond': 'Mandeln', 'cn_alu_ingots': 'Aluminiumbarren',
    'cn_alu_profiles': 'Aluminiumprofile', 'cn_anhydrous_ammonia': 'Wasserfreies Ammoniak',
    'cn_ammunition': 'Munition', 'cn_apples': 'Äpfel', 'cn_arsenic': 'Arsen',
    'cn_atlantic_cod_fillet': 'Atlantischer Kabeljau-Filet', 'cn_backflow_preventers': 'Rückflussverhinderer',
    'cn_barley': 'Gerste', 'cn_basil': 'Basilikum', 'cn_batteries': 'Batterien',
    'cn_beans': 'Bohnen', 'cn_beef_meat': 'Rindfleisch', 'cn_beverages': 'Getränke',
    'cn_big_bags_seeds': 'Große Säcke mit Samen', 'cn_boric_acid': 'Borsäure',
    'cn_bottled_water': 'Flaschenwasser', 'cn_brake_fluid': 'Bremsflüssigkeit',
    'cn_brake_pads': 'Bremsbeläge', 'cn_red_bricks': 'Rote Ziegel',
    'cn_canned_beans': 'Dosenbohnen', 'cn_canned_beef': 'Dosenrindfleisch',
    'cn_canned_pork': 'Dosen-Schweinefleisch', 'cn_canned_tuna': 'Dosenthunfisch',
    'cn_canned_sardines': 'Dosensardinen', 'cn_bottled_carbonated_water': 'Kohlensäurehaltiges Wasser',
    'cn_carrots': 'Karotten', 'cn_cars': 'Autos', 'cn_cauliflower': 'Blumenkohl',
    'cn_caviar': 'Kaviar', 'cn_cement': 'Zement', 'cn_cheese': 'Käse',
    'cn_chemicals': 'Chemikalien', 'cn_chemical_sorbent': 'Chemischer Sorptionsmittel',
    'cn_chicken_meat': 'Hühnerfleisch', 'cn_chimney_systems': 'Schornsteinsysteme',
    'cn_chlorine': 'Chlor', 'cn_chocolate': 'Schokolade', 'cn_clothes': 'Kleidung',
    'cn_coal': 'Kohle', 'cn_coconut_milk': 'Kokosmilch', 'cn_coconut_oil': 'Kokosöl',
    'cn_computer_processors': 'Computerprozessoren', 'cn_concr_beams': 'Betonträger',
    'cn_concr_centering': 'Betonzentrierung', 'cn_concr_stair': 'Betontreppe',
    'cn_concentrate_juices': 'Konzentrierte Säfte', 'cn_contamin': 'Kontaminierte Substanzen',
    'cn_containerized_trees': 'Containerisierte Bäume', 'cn_copper_roof_gutters': 'Kupferdachrinnen',
    'cn_corks': 'Korken', 'cn_cottage_cheese': 'Hüttenkäse', 'cn_cotton_harvester': 'Baumwollernter',
    'cn_crawler_carrier': 'Raupentransporter', 'cn_cut_flowers': 'Schnittblumen',
    'cn_cyanide': 'Zyanid', 'cn_desinfection': 'Desinfektionsmittel',
    'cn_diesel': 'Diesel', 'cn_diesel_generators': 'Dieselgeneratoren', 'cn_wheel_loader': 'Radlader',
    'cn_backhoe_loader': 'Baggerlader', 'cn_dryers': 'Trockner', 'cn_drymilk': 'Trockenmilch',
    'cn_dynamite': 'Dynamit', 'cn_electronics': 'Elektronik', 'cn_electric_wiring': 'Elektrische Verkabelung',
    'cn_tank': 'Leerer Tank', 'cn_empty_barrels': 'Leere Fässer', 'cn_empty_palettes': 'Leere Paletten',
    'cn_empty_spool': 'Leere Spule', 'cn_empty_wine_barrels': 'Leere Weinfässer',
    'cn_empty_wine_bottles': 'Leere Weinflaschen', 'cn_ethane': 'Ethan', 'cn_excavator': 'Bagger',
    'cn_excavated_soil': 'Ausgegrabener Boden', 'cn_exhaust_systems': 'Auspuffsysteme',
    'cn_explosives': 'Sprengstoffe', 'cn_fertilizer': 'Dünger', 'cn_fireworks': 'Feuerwerk',
    'cn_fish_chips': 'Fischchips', 'cn_food_oil': 'Speiseöl', 'cn_forklifts': 'Gabelstapler',
    'cn_fresh_fish': 'Frischer Fisch', 'cn_frozen_hake': 'Gefrorener Hecht',
    'cn_froz_octopi': 'Gefrorene Oktopusse', 'cn_fresh_herbs': 'Frische Kräuter',
    'cn_tanker': 'Treibstofftanker', 'cn_fuel_oil': 'Heizöl', 'cn_fuel_tanks': 'Treibstofftanks',
    'cn_furniture': 'Möbel', 'cn_garlic': 'Knoblauch', 'cn_pck_glass': 'Verpacktes Glas',
    'cn_gnocchi': 'Gnocchi', 'cn_goat_cheese': 'Ziegenkäse', 'cn_granite_cubes': 'Granitwürfel',
    'cn_grapes': 'Trauben', 'cn_graph_grease': 'Graphitfett', 'cn_grass_rolls': 'Grasrollen',
    'cn_gravel': 'Kies', 'cn_guard_rails': 'Leitplanken', 'cn_gummy_bears': 'Gummibärchen',
    'cn_harvesting_bins': 'Erntebehälter', 'cn_hot_chem': 'Heiße Chemikalien', 'cn_honey': 'Honig',
    'cn_horse_trailer': 'Pferdeanhänger', 'cn_aircond': 'Klimaanlagen', 'cn_hwaste': 'Gefährlicher Abfall',
    'cn_hydrochlor': 'Salzsäure', 'cn_hydrogen': 'Wasserstoff', 'cn_ibc_containers': 'IBC-Container',
    'cn_icecream': 'Eiscreme', 'cn_canned_iced_coffee': 'Dosen-Eiskaffee', 'cn_pipes': 'Eisenrohre',
    'cn_kerosene': 'Kerosin', 'cn_ketchup': 'Ketchup', 'cn_lamb_stomachs': 'Lammmägen',
    'cn_largetubes': 'Große Rohre', 'cn_large_containers': 'Große Container', 'cn_lavender': 'Lavendel',
    'cn_lead': 'Blei', 'cn_limonades': 'Limonaden', 'cn_luxury_suvs': 'Luxus-SUVs',
    'cn_volvo_trucks': 'Volvo-LKWs', 'cn_caravans': 'Wohnwagen', 'cn_suvs': 'SUVs',
    'cn_tractors': 'Traktoren', 'cn_train_parts': 'Zugteile', 'cn_carbon_black_powder': 'Kohlenschwarz-Pulver',
    'cn_chewing_gums': 'Kaugummis', 'cn_flour': 'Mehl', 'cn_fluorine': 'Fluor',
    'cn_liver_paste': 'Leberpastete', 'cn_live_cattle': 'Lebendes Vieh', 'cn_live_pigs': 'Lebende Schweine',
    'cn_logs': 'Stämme', 'cn_lpg': 'Flüssiggas', 'cn_lumber': 'Bauholz',
    'cn_packed_lumber': 'Verpacktes Bauholz', 'cn_luxury_yacht': 'Luxusjacht', 'cn_magnesium': 'Magnesium',
    'cn_maple_syrup': 'Ahornsirup', 'cn_marble_block': 'Marmorblock', 'cn_mason_jars': 'Einmachgläser',
    'cn_material_handler': 'Materialhandler', 'cn_medical_equipment': 'Medizinisches Gerät',
    'cn_medical_vaccines': 'Medizinische Impfstoffe', 'cn_mercuric': 'Quecksilber',
    'cn_metal_beams': 'Metallträger', 'cn_metal_cans': 'Metalldosen', 'cn_milk': 'Milch',
    'cn_motorcycles': 'Motorräder', 'cn_motor_oil': 'Motoröl', 'cn_motorcycle_tires': 'Motorradreifen',
    'cn_mozzarela': 'Mozzarella', 'cn_metal_coil': 'Metallspule', 'cn_natural_rubber': 'Naturgummi',
    'cn_neon': 'Neon', 'cn_nitrocel': 'Nitrocellulose', 'cn_nitrogen': 'Stickstoff',
    'cn_nonalcoholic_beer': 'Alkoholfreies Bier', 'cn_nuts': 'Nüsse', 'cn_nylon_cord': 'Nylonfaden',
    'cn_oil': 'Öl', 'cn_oil_filters': 'Ölfilter', 'cn_olives': 'Oliven', 'cn_olive_oil': 'Olivenöl',
    'cn_olive_trees': 'Olivenbäume', 'cn_onion': 'Zwiebeln', 'cn_oranges': 'Orangen', 'cn_ore': 'Erz',
    'cn_outdoor_floor_tiles': 'Außenbodenfliesen', 'cn_trailers': 'Anhänger (overweight)',
    'cn_packaged_food': 'Verpackte Lebensmittel', 'cn_paper': 'Papier', 'cn_pasta': 'Pasta',
    'cn_pears': 'Birnen', 'cn_peas': 'Erbsen', 'cn_performance_fork': 'Leistungsstarke Gabeln',
    'cn_pesticide': 'Pestizid', 'cn_pesto': 'Pesto', 'cn_petrol': 'Benzin', 'cn_pet_food': 'Tierfutter',
    'cn_phosphor': 'Phosphor', 'cn_plant_substrate': 'Pflanzsubstrat', 'cn_plastic': 'Plastik',
    'cn_plastic_film_rolls': 'Plastikfolienrollen', 'cn_plastic_pipes': 'Plastikrohre',
    'cn_plumbing_supplies': 'Sanitärbedarf', 'cn_plums': 'Pflaumen', 'cn_pnut_butter': 'Erdnussbutter',
    'cn_polystyrene_boxes': 'Styroporboxen', 'cn_pork_meat': 'Schweinefleisch', 'cn_post_packages': 'Postpakete',
    'cn_potahydro': 'Kaliumhydroxid', 'cn_potassium': 'Kalium', 'cn_potatoes': 'Kartoffeln',
    'cn_potted_flowers': 'Topfblumen', 'cn_precast_stairs': 'Fertigtreppen',
    'cn_high_pressure_slide_valves': 'Hochdruck-Schieber', 'cn_propane': 'Propan',
    'cn_prosciutto': 'Prosciutto', 'cn_protective_clothing': 'Schutzkleidung', 'cn_pumps': 'Pumpen',
    'cn_radiators': 'Radiatoren', 'cn_reflective_posts': 'Reflektierende Pfosten',
    'cn_re_bars': 'Bewehrungsstäbe', 'cn_rice': 'Reis', 'cn_roofing_felt': 'Dachpappe',
    'cn_rooflights': 'Dachlichter', 'cn_roof_tiles': 'Dachziegel', 'cn_rye': 'Roggen',
    'cn_salmon_fillet': 'Lachsfilet', 'cn_salt_spices': 'Salz und Gewürze', 'cn_sand': 'Sand',
    'cn_sandwich_panels': 'Sandwichpaneele', 'cn_sausages': 'Würste', 'cn_sawpanels': 'Sägepaneele',
    'cn_scaffoldings': 'Gerüste', 'cn_scooters': 'Scooter', 'cn_scrap_metals': 'Schrottmetalle',
    'cn_sealed_bearings': 'Versiegelte Lager', 'cn_sheep_wool': 'Schafwolle', 'cn_shock_absorbers': 'Stoßdämpfer',
    'cn_silica': 'Kieselsäure', 'cn_smoked_eel': 'Geräucherter Aal', 'cn_smoked_sprats': 'Geräucherte Sprotten',
    'cn_sodchlor': 'Natriumchlorid', 'cn_sodhydro': 'Natriumhydroxid', 'cn_sodium': 'Natrium',
    'cn_soy_milk': 'Sojamilch', 'cn_spherical_valves': 'Kugelhähne', 'cn_square_tubing': 'Vierkantprofile',
    'cn_steel_cord': 'Stahlcord', 'cn_stones': 'Steine', 'cn_stone_dust': 'Steinstaub',
    'cn_stone_wool': 'Steinwolle', 'cn_straw_bales': 'Strohballen', 'cn_sugar': 'Zucker',
    'cn_sulfuric': 'Schwefelsäure', 'cn_tableware': 'Geschirr', 'cn_rough_terrain_forklift': 'Geländegabelstapler',
    'cn_tomatoes': 'Tomaten', 'cn_toys': 'Spielzeug', 'cn_train_part': 'Zugteil',
    'cn_train_part2': 'Zugteil 2', 'cn_transmissions': 'Getriebe', 'cn_truck_battery': 'LKW-Batterie',
    'cn_truck_rims': 'LKW-Felgen', 'cn_truck_tyres': 'LKW-Reifen', 'cn_tyres': 'Reifen',
    'cn_used_car_batteries': 'Gebrauchte Autobatterien', 'cn_used_packaging': 'Gebrauchte Verpackung',
    'cn_used_plastics': 'Gebrauchte Plastik', 'cn_vent_tube': 'Lüftungsrohr', 'cn_vinegar': 'Essig',
    'cn_watermelons': 'Wassermelonen', 'cn_water_tank': 'Wassertank', 'cn_wheat': 'Weizen',
    'cn_windmill_engine': 'Windmühlenmotor', 'cn_windmill_tube': 'Windmühlentube',
    'cn_wooden_beams': 'Holzbalken', 'cn_wood_bark': 'Holzrinde', 'cn_work_clothes': 'Arbeitskleidung',
    'cn_wshavings': 'Holzspäne', 'cn_yogurt': 'Yoghurt', 'cn_young_seedlings': 'Junge Setzlinge',
    'cn_waste_container': 'Abfallcontainer',
}

translations_trailer = {
    'curtainside': 'Planenauflieger', 'dryvan': 'Trockenfracht', 'insulated': 'Isoliert',
    'refrigerated': 'Kühlfracht', 'chemtank': 'Chemietank', 'dumper': 'Kipper',
    'flatbed_brck': 'Flachbett (Ziegel)', 'container': 'Container', 'flatbed': 'Flachbett',
    'foodtank': 'Lebensmitteltank', 'fueltank': 'Treibstofftank', 'gastank': 'Gastank',
    'livestock': 'Viehtransport', 'log': 'Holztransport', 'lowbed': 'Tieflader',
    'lowboy': 'Tieflader (US)', 'silo': 'Silo',
}

# --- HELFER FUNKTIONEN ---

def clean_cargo_name(raw_id):
    raw_s = str(raw_id).lower().strip()
    if raw_s in translations_cargo:
        return translations_cargo[raw_s]
    search_term = f"cn_{raw_s.replace('cargo.', '')}"
    if search_term in translations_cargo:
        return translations_cargo[search_term]
    return raw_s.replace('cn_', '').replace('cargo.', '').replace('_', ' ').title()

def format_axles(trailer_id):
    config_str = str(trailer_id).lower()
    if "hct" in config_str: return "Gigaliner (HCT)"
    nums = re.findall(r'\d+', config_str.split('.')[-2] if '.' in config_str else config_str)
    if nums:
        total = sum(int(n) for n in nums)
        if total > 15: total = int(nums[0])
        prefix = "Single " if "single" in config_str else "Double " if "double" in config_str else ""
        return f"{prefix}{total} Achsen"
    return "Standard Achsen"

# --- HAUPT ANWENDUNG ---

class ETS2App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ETS2 Cargo Planer by AMMOKNOXX")
        self.geometry("1150x900")
        ctk.set_appearance_mode("dark")

        self.cur_cargo = None
        self.cur_trailer = None
        self.shown_trailers = pd.DataFrame()

        try:
            self.trailers_df = pd.read_csv('trailers_clean.csv').fillna(0)
            self.trailers_df['empty_mass'] = pd.to_numeric(self.trailers_df['empty_mass'], errors='coerce').fillna(0)
            self.trailers_df['gross_weight'] = pd.to_numeric(self.trailers_df['gross_weight'], errors='coerce').fillna(35000)

            cargos_raw = pd.read_csv('cargos_clean.csv').fillna(0)
            self.cargos_df = cargos_raw[~cargos_raw['body_types'].str.startswith('_', na=False)].copy()
            self.cargos_df['display_name'] = self.cargos_df['name'].apply(clean_cargo_name)
            self.cargos_df = self.cargos_df.sort_values('display_name')
        except Exception as e:
            tk.messagebox.showerror("Datenfehler", f"Dateien konnten nicht geladen werden:\n{e}")
            self.destroy()
            return

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = ctk.CTkFrame(self, fg_color=PRI_RED, height=70, corner_radius=0)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")
        ctk.CTkLabel(self.header, text="ETS2 Cargo Planer", font=("Impact", 32), text_color="white").pack(pady=15)

        # Linke Seite
        self.f_left = ctk.CTkFrame(self, fg_color="transparent")
        self.f_left.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        ctk.CTkLabel(self.f_left, text="1. FRACHT AUSWÄHLEN", font=("Arial", 16, "bold")).pack(anchor="w")
        self.search = ctk.CTkEntry(self.f_left, placeholder_text="Fracht suchen...", border_color=PRI_RED, height=35)
        self.search.pack(fill="x", pady=10)
        self.search.bind("<KeyRelease>", lambda e: self.update_cargo_list())
        self.list_cargo = tk.Listbox(self.f_left, bg="#1d1d1d", fg="white", font=("Consolas", 12), borderwidth=0, selectbackground=PRI_RED, highlightthickness=0)
        self.list_cargo.pack(fill="both", expand=True)
        self.list_cargo.bind("<<ListboxSelect>>", self.on_select_cargo)

        # Rechte Seite
        self.f_right = ctk.CTkFrame(self, fg_color="#2a2a2a")
        self.f_right.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        # NEU: Profil-Bonus Bereich
        self.f_bonus = ctk.CTkFrame(self.f_right, fg_color="#1d1d1d", border_width=1, border_color=ADR_ORANGE)
        self.f_bonus.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(self.f_bonus, text="PROFIL-BONI", font=("Arial", 12, "bold"), text_color=ADR_ORANGE).grid(row=0, column=0, columnspan=2, pady=5)
        
        ctk.CTkLabel(self.f_bonus, text="Fahrer-Level:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.lvl_input = ctk.CTkEntry(self.f_bonus, width=60, placeholder_text="0")
        self.lvl_input.insert(0, "0")
        self.lvl_input.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(self.f_bonus, text="Fernfahrt-Skill (0-6):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.skill_input = ctk.CTkEntry(self.f_bonus, width=60, placeholder_text="0")
        self.skill_input.insert(0, "0")
        self.skill_input.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(self.f_right, text="2. KOMPATIBLE TRAILER", font=("Arial", 16, "bold")).pack(pady=10)
        self.list_trailer = tk.Listbox(self.f_right, bg="#1d1d1d", fg="white", font=("Consolas", 11), borderwidth=0, selectbackground=PRI_RED, highlightthickness=0, height=8)
        self.list_trailer.pack(fill="x", padx=20)
        self.list_trailer.bind("<<ListboxSelect>>", self.on_select_trailer)

        self.km_input = ctk.CTkEntry(self.f_right, placeholder_text="Distanz in km eingeben...", height=40, font=("Arial", 14))
        self.km_input.pack(pady=20, padx=50, fill="x")
        
        ctk.CTkButton(self.f_right, text="PLANUNG BERECHNEN", fg_color=PRI_RED, hover_color="#8a0404", font=("Arial", 14, "bold"), height=45, command=self.calc).pack(pady=5)

        self.res_box = ctk.CTkFrame(self.f_right, fg_color="#151515", border_width=1, border_color=PRI_RED)
        self.res_box.pack(fill="both", expand=True, padx=20, pady=20)
        self.res_label = ctk.CTkLabel(self.res_box, text="Wähle Fracht und Trailer aus...", font=("Consolas", 14), justify="left")
        self.res_label.pack(pady=20, padx=15)

        self.update_cargo_list()

    def update_cargo_list(self):
        self.list_cargo.delete(0, "end")
        q = self.search.get().lower()
        self.current_shown_cargos = self.cargos_df[self.cargos_df['display_name'].str.lower().str.contains(q)].copy()
        for name in self.current_shown_cargos['display_name']:
            self.list_cargo.insert("end", f" {name}")

    def on_select_cargo(self, e):
        sel = self.list_cargo.curselection()
        if not sel: return
        self.cur_cargo = self.current_shown_cargos.iloc[sel[0]]
        self.cur_trailer = None
        required_bodies = [b.strip() for b in str(self.cur_cargo['body_types']).split(',')]
        self.shown_trailers = self.trailers_df[self.trailers_df['body_type'].isin(required_bodies)].copy()
        self.list_trailer.delete(0, "end")
        if self.shown_trailers.empty:
            self.list_trailer.insert("end", " KEIN KOMPATIBLER TRAILER GEFUNDEN")
        else:
            for _, r in self.shown_trailers.iterrows():
                t_name = translations_trailer.get(r['body_type'], r['body_type'].title())
                t_info = format_axles(r['trailer_id'])
                mass = int(r['empty_mass'])
                self.list_trailer.insert("end", f" {t_name:<15} | {t_info:<18} | {mass:>5}kg")
        self.res_label.configure(text="Bitte jetzt den Trailer wählen...", text_color="white")

    def on_select_trailer(self, e):
        sel = self.list_trailer.curselection()
        if not sel or self.shown_trailers.empty: return
        self.cur_trailer = self.shown_trailers.iloc[sel[0]]
        self.res_label.configure(text="Bereit zur Berechnung.", text_color="white")

    def calc(self):
        if self.cur_cargo is None or self.cur_trailer is None:
            self.res_label.configure(text="Fehler: Auswahl unvollständig!", text_color="red")
            return
        
        try:
            km = float(self.km_input.get().replace(',', '.'))
            lvl = int(self.lvl_input.get() if self.lvl_input.get() else 0)
            skill = int(self.skill_input.get() if self.skill_input.get() else 0)
            
            cargo_mass = float(self.cur_cargo['mass'])
            total_mass = cargo_mass + float(self.cur_trailer['empty_mass'])
            max_weight = float(self.cur_trailer['gross_weight'])
            
            # Leistung (tkm) mit Gesamtgewicht
            tkm = (total_mass / 1000.0) * km
            
            # Basis-Verdienst nach deiner economy_data.sii
            fixed_rev = 600
            rev_per_km_base = 15
            cargo_coef = float(self.cur_cargo['reward_per_km'])
            
            base_reward = fixed_rev + (km * rev_per_km_base * cargo_coef)
            
            # Boni berechnen (Werte aus deiner SII-Datei)
            lvl_bonus = base_reward * (lvl * 0.015)  # reward_bonus_level: 0.015
            dist_bonus = 0
            if km > 250: # Fernfahrt-Bonus meist ab 250km aktiv
                dist_bonus = base_reward * (skill * 0.05) # reward_bonus_long_dist: 0.05
            
            total_reward = base_reward + lvl_bonus + dist_bonus
            
            adr = str(self.cur_cargo.get('adr_class', '0')).strip()
            is_adr = adr not in ['0', '', 'nan']
            adr_text = f"KLASSE {adr}" if is_adr else "KEIN ADR"
            
            weight_warning = " [ÜBERGEWICHT!]" if total_mass > max_weight else ""

            res_text = (
                f"LADUNG:    {self.cur_cargo['display_name']}\n"
                f"ADR-STATUS: {adr_text}\n"
                f"{'-'*45}\n"
                f"NETTO-LAST: {cargo_mass:,.0f} kg\n"
                f"GESAMT-GEW: {total_mass:,.0f} kg / {max_weight:,.0f} kg{weight_warning}\n"
                f"DISTANZ:    {km:,.1f} km\n"
                f"{'-'*45}\n"
                f"LEISTUNG:   {tkm:,.2f} tkm\n"
                f"BASIS:      {base_reward:,.2f} €\n"
                f"BONI (Lvl/Skill): +{(lvl_bonus + dist_bonus):,.2f} €\n"
                f"VERDIENST:  {total_reward:,.2f} €"
            )
            
            self.res_label.configure(text=res_text, text_color=ADR_ORANGE if is_adr else "white")

        except ValueError:
            self.res_label.configure(text="Fehler: Ungültige Zahlenwerte!", text_color="red")
        except Exception as e:
            self.res_label.configure(text=f"Fehler: {e}", text_color="red")

if __name__ == "__main__":
    app = ETS2App()
    app.mainloop()