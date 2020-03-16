import tkinter as tk
import tkinter.ttk
import arrow
import sys
import os
from tkcalendar import Calendar, DateEntry
from odps import ODPS,options


# Level 3 sub category

movies1 = {"Bags and Travel": ['Backpacks','Backpacks Trolley','Bags','Backpacks','Business Bags','Crossbody Bags','Messenger Bags','Tote Bags','Wallets & Accessories','Laptop Bags','Luggage','Travel Accessories','Travel Bags','Backpacks','Card Holders','Coin Purses & Pouches','Key Holders','Backpacks','Clutches','Cross Body & Shoulder Bags','Top-Handle Bags','Tote Bags','Wallets & Accessories','Wristlets'],
          "Bedding & Bath": ['Bath Mats','Bath Towels','Bathrobes','Bathroom Counter Storage','Bathroom Mirrors','Bathroom Scales','Bathroom Shelving','Linen Towers & Cabinets','Shower Caddies & Hangers','Shower Curtains','Toilet Brushes','Toilet Covers','Toilet Roll Holders','Towel Rails & Warmers','Bed Runners & Skirts','Bed Sheets','Bedding Accessories','Bedding Sets','Blankets & Throws','Comforters, Quilts & Duvets','Electric Blankets','Mattress Pads','Mattress Protectors','Pillow Cases','Pillow Protectors','Pillows & Bolsters'],
          "Computers & Laptops": ['Adapters & Cables','Blank Media','Bluetooth Adapters','Card Reader','Cooling PadsCooling Stands','Drawing Tools','External DVD Writers','Fingerprint Reader','Gadgets','Gaming Headphones','Keyboards','Laptop Batteries','Laptop stands','Mac Accessories','Mice','Monitor Screen Filters','Monitor Stands','Monitors','Mousepads','PC Audio','Power Cord & Adaptors','Speakers','Surge Protector','TV Tuners','USB Fans','USB Hubs','USB Lighting','Uninterrupted Power Supply','Webcams','Desktop Casings','Fans & Heatsinks','Front Bay Devices','Graphic Cards','Motherboards','Power Supply Units','Processors','RAM','Single Board Computer','Sound cards','Water Cooling System','All-In-One','DIY','Gaming','2-in-1s','All-purpose','Basic','Chromebooks','Macbooks','Traditional Laptops','Ultrabooks','Access Points','Airport Routers','Mobile Broadband','Modems','Network Gadgets','Network Interface Cards','Network adaptors','Range extender','Routers','Switches','Wireless USB Adapters','PC Games','3D Printing','Fax machines','Ink','Printer cutter','Printer memory modules','Printer stands','Printers'],
          "Cameras": ['Batteries','Battery Chargers','Camera Cases Covers and Bags','Camera Remote Controls','Camera Screen Protector','Dry Box','Flashes','Gimbals & Stabilizers','Gimbals & Stabilizers Accessories','Lighting & Studio Equipment','Memory Cards','Sports & Action Camera Accessories','Straps','Tripods & Monopods','Viewfinders','Body Only','Sets','Drone Accessories','Drones','Lomography','Mini Cameras','Spy Cameras','Toy Cameras','Instant Camera Accessories','Instant Camera Films','Instant Cameras','DSLRs Lenses','Lens Accessories','Mirrorless Lenses','Other Lenses','Smartphone Lenses','Binoculars','Monoculars','Optics Accessories','Telescopes','Point & Shoot','Underwater Digital Cameras','CCTV Security Cameras','CCTV Security Systems','Dummy Cameras','IP Security Cameras','IP Security Systems','360 Cameras','Professional Video Camera','Sports & Action Camera','Video Camera'],
          "Digital Goods": ['Insurance','Digital Games','Game Codes','Game Keys','Gift Cards','Softwares','Installation','Maintenance','Repair','Replacement','Activities & Entertainment','Activities and Entertainment','Beauty & Wellness','Beauty and Wellness','Fashion & Apparel','Fashion and Apparel','Food and Beverage','Food and Beverages','Home','Hotel & Travel','Hotel and Travel','Linehaul Service'],
          "Fashion": ['Accessories','Clothing','Shoes','Accessories','Ethnic Wear','Muslim Wear','Shoes','Lingerie, Sleep & Lounge'],
          "Furniture & Dacor": ['Bedroom Furniture','Furniture Protectors & Parts','Gaming Furniture','Hallway & Entry Furniture','Home Office Furniture','Kids Furniture','Kitchen & Dining Furniture','Living Room Furniture','Outdoor Furniture','Aromatherapy and Home Fragrance','Artificial Flowers & Plants','Candles & Candleholders','Clocks','Curtains','Cushions & Covers','Decorative Accents','Decorative Bowls','Decorative Door Stops','Mirrors','Picture Frames','Room Dividers & Screens','Rugs & Carpets','Seasonal','Tapestries & Hangings','Vases & Vessels','Wall DÃ©cor','Wall Stickers & Decals','Bathroom Lighting','Ceiling Lights','Floor Lamps','Lamp Shades','Light Bulbs','Lighting Fixtures & Components','Outdoor Lighting','Specialty Lighting','Table Lamps','Wall Lights & Sconces','Bike & Sports Racks','Deck Boxes & Balcony Storage','Medicine & First Aid Storage','Shoe Organisers','Space Savers','Storage Bins & Baskets','Wardrobe Organisers'],
          "Groceries": ['Bread','Breakfast & Treats','Cakes & Sweet Pies','Condiment Dressing','Cooking Ingredients','Home Baking & Sugar','Asian Health Drinks','Coffee','Energy Drink','Flavoring Syrups','Hot Chocolate and Nutrition Drinks','Juices','Powdered drink mixes','Soft Drinks','Tea','UHT, Milk & Milk Powder','Water','Bars','Breakfast Cereals','Granola','Instant Breakfast Drinks','Jams, Honey & Spreads','Oatmeals','Pancake & Waffle Mixes','Candy Assortments','Caramels & Toffee','Chewing Gum & Mints','Chocolate','Festive Boxed','Marshamallows','Nuts & Fruits','Other Sweets','Canned Food','Condiments & Pickles','Dried Goods','Grains, Beans &Pulses','Instant & Ready to Eat','Jarred Food','Noodles, Pasta & Rice','Cigarettes','Cigars','Lighters','Matches','Cheese','Chilled Drinks','Convenience Foods','Deli','Desserts','Milk, Butter & Eggs','Yoghurt','Fresh Fruit','Fresh Herbs & Spices','Fresh Vegetables','Mushrooms','Other Vegetables','Salad','Bread, Bagels & Pancakes','Frozen Desserts','Ice Cream','Meat','Mock Meat & Seafood','Seafood','Vegetables & Fruits'],
          "Health & Beauty": ['Bath & Body Accessories','Body & Massage Oils','Body Moisturizers','Body Scrubs','Body Soaps & Shower Gels','Breast Care','Foot Care','Gifts & Value Sets','Hair Removal','Hand Care','Sun Care for Body','Talcum Powder','Body Slimming & Electric Massagers','Foot Relief Accessories & Tools','Hair Removal Accessories','Hair Removal Appliances','Hair Styling Appliances','Portable Saunas','Skin Care Tools','Beauty Supplements','Sports Nutrition','Weight Management','Well Being','Men','Mens Fragrance','Unisex','Women','Facial Sets','Conditioner','Hair Care Accessories','Hair Coloring','Hair Oils','Hair Styling','Hair Treatments','Shampoo','Body','Eyes','Face','Lips','Makeup Accessories','Makeup Palettes & Sets','Makeup Removers','Nails','Compression Stockings','First Aid Supplies','Health Accessories','Health Monitors & Tests','Hospital Beds','Injury Support and Braces','Medical Tests','Nebulizer & Aspirators','Ointments and Creams','Pedometers','Scale & Body Fat Analyzers','Stethoscopes','Wheelchairs','Bath & Body','Deodorants','Hair Care','Shaving & Grooming','Skin Care','Anti-Inflammatory','Antibacterial & Antifungal','Antidote','Antiseptics','Blood Glucose Control','Constipation','Coughs, Colds & Flu','Dehydration','Diabetic','Diagnostic Kits','Diarrhea & Vomiting','Eye, Nose, Throat Care','Herbal','Indigestion & Heartburn','Pain Relief & Fever','Scar Care','Topical Analgesics','Adult Diapers & Incontinence','Ear Care','Eye Care','Feminine Care','Oral Care','Personal Safety & Security','Performance Enhancement Supplement','Beauty Services','Event Management','Freelancer Services','Photography Services','Tattoo','Condoms','Lubricants','Sensual Toys','Dermacare','Face Mask & Packs','Face Scrubs & Exfoliators','Facial Cleansers','Lip Balm and Treatment','Moisturizers and Cream','Serum & Essence','Sunscreen and Aftersun','Toner & Mists'],
          "Home Appliances": ['Air Conditioner Accessories','Air Purifier Accessories','Coffee Machine Accessories','Cooktop Parts & Accessories','Dishwasher Parts & Accessories','Fan Parts & Accessories','Freezer Parts & Accessories','Fryer and Air Fryer Accessories','Gas Stove Parts & Accessories','Microwave Parts & Accessories','Range Hood Parts & Accessories','Refrigerator Parts & Accessories','Rice Cookers and Steamers Accessories','Sewing Machine Parts & Accessories','Small Kitchen Appliance Parts & Accessories','Specialty Cookware Accessories','Toasters and Sandwich Makers Accessories','Vacuum Cleaners Accessories','Ventilation Parts & Accessories','Wall Oven Parts & Accessories','Washer & Dryer Parts & Accessories','Water Dispenser Accessories','Water Heater Parts & Accessories','Water Purifiers & Filters Accessories','Air Conditioning','Air Treatment','Exhaust Fans','Fans','Heaters','Water Heaters','Garment Presses','Garment Steamers','Irons','Cooktops & Ranges','Dishwashers & Parts','Freezers','Gas Stoves','Microwaves & Parts','Ovens','Range Hoods','Refrigerators','Warming Drawers','Water Dispensers, Purifiers & Filters','Wine Cellars','Cooktops','Dish Washers & Dryers','Hoods','Microwaves & Ovens','Ranges & Hobs','Washers & Dryers'],
          "Kitchen & Dining": ['Bakeware Dishes','Bakeware Sets','Baking Tools & Accessories','Baking Trays & Pans','Cake Decorating Tools','Wire Racks','Coffee Makers & Grinders','Coffee Making Accessories','Coffee, Tea & Espresso','Creamer & Sugar Bowls','Milk Frothers','Tea Making Accessories','Teapots & Coffee Servers','Casserole Pots','Cookware Sets','Dutch Oven & Braziers','Griddle & Grills','Pots & Pans','Roasting Trays','Specialty Cookware','Steamers, Stock & Pasta Pots','Stove Kettles','Stovetop Pressure Cookers','Woks & Stir-Fry Pans', 'Bowls','Cutlery','Dining Sets','Disposable Dinnerware','Plates','Bar & Wine Tools','Cups, Mugs & Saucers','Decanters','Everyday Glassware','Gravity Water Dispenser','Jugs & Pitchers','Specialty Glassware','Wine & Champagne Glasses','Aprons','Cloth Napkins','Dish Cloth & Towels','Placemats & Coasters','Potholders, Mitts & Cozies','Table Cloths & Runners','Table Linen Accessories','Condiment & Spice Racks','Dishracks & Sink accessories','Drink Bottles','Food Storage & Dispensers','Kitchen Canisters & Jars','Kitchen Organizers','Lunch Bags & Boxes','Pot Racks','Shopping Trolleys & Carriers','Thermal Flasks & Containers','Wine Racks','Can Openers','Cheese Tools','Colanders & Food Strainers','Cooking Utensils','Fruit & Vegetable Tools','Graters, Peelers & Slicers','Knives & Accessories', 'Measuring Tools & Scales','Meat & Poultry Tools','Mixing Bowls','Mortar & Pestle','Oil Sprayers & Dispensers','Pasta, Noodle & Pizza Tools','Preparation & Cutting Boards','Seasoning & Spice Tools','Specialty Kitchen Tools','Thermometers & Timers','Bread Baskets & Trays','Butter Dishes','Cake & Tiered Stands','Cheese Boards & Platters','Cruets & Condiment Sets','Divided Serving Dishes','Food Warmers','Gravy Boats','Lazy Susans','Salad Bowls','Serving Bowls','Serving Platters','Serving Trays','Serving Utensils','Trivets','Tureens'],
          "Laundry & Cleaning": ['Brooms, Mops & Sweepers','Brushes, Sponges & Wipers','Cleaning Buckets & Tubs','Cleaning Gloves','Cleaning Products','Dusters & Dust Cloths','Garbage & Recycling Bins','Trash Bags & Liners','Clothes Hangers & Pegs','Clothes Line & Drying Racks','Ironing Boards','Laundry & Ironing Tools','Laundry Bags & Wash Balls','Laundry Baskets & Hampers'],
          "Media, Music & Books": ['Calendars','Chinese Books','English Books','Local Books','Children Magazines','Design Magazines','Education Magazines','Entertainment Magazines','Fashion Magazines','Health and Beauty Magazines','IT Magazines','Jewelry Magazines','Knowledge Magazines','Life Magazines','Lifestyle Magazines','Mens Lifestyle Magazines','Pets Magazines','Teen Magazines','Womens Lifestyle Magazines','Action','Box Sets','Comedy','Educational','Alternative Rock','Blues','Children','Classical','Country','Electronic','Folk','Inspirational','Local Music','Metal & Hard Rock','Movie Soundtracks','Religion','Rock','Band & Orchestra','Bass Guitars','DJ, Karaoke & Electronic Music','Drums & Percussion','Guitars','Instrument Accessories','Keyboards & Pianos','Others','Pro & DJ Headphones','Traditional instruments','Woodwind','Chinese eBooks','English eBooks','Local eBooks'],
          "Mobiles & Tablets": ['Cables & Converters','Car Chargers','Car Mounts','Docks & Stands','Fashion Accessories','Fashion Mobile Accessories','Parts & Tools','Phone Batteries','Phone Camera Flash Lights','Phone Cases','Power Banks','Screen Protectors','Selfie Sticks','Wall Chargers','Wireless Chargers','Cases & Covers','Stylus Pens'],
          "Mother & Baby": ['Backpacks & Carriers','Car Seats','Harnesses & Leashes','Kids Bags & Luggage','Strollers','Swings, Jumpers & Bouncers','Walkers','Colic & Gas Relief','Aromatherapy','Bathing Tubs & Seats','Bubble Bath','Grooming & Healthcare Kits','Shampoo & Conditioners','Skin Care','Soaps, Cleansers & Bodywash','Washcloths & Towels','Bathroom Safety','Cabinet Locks & Straps','Edge & Corner Guards','Safety Caps','Sanitizers','Boys','Girls','New Born Unisex (0 - 6 mnths)','Cloth Diapers & Accessories','Diaper Bags','Diapering Care','Disposable Diapers','Potty Training','Wipes & Holders','Baby & Toddler Foods','Bottle-Feeding','Breastfeeding','Highchairs & Booster Seats','Milk Formula','Utensils','Gift Sets','Maternity Accessories','Maternity Wear','Baby Furniture','Mattresses & Bedding','Nursery Décor','Storage & Organization','Leashes & Cases','Pacifiers'],
          "Motors": ['Auto Oils & Fluids','Auto Parts & Spares','Auto Tires & Wheels','Auto Tools & Equipment','Batteries & Accessories','Car Audio','Car Electronics Accessories','Car Safety & Security','Car Video','Convertibles','Coupes','Exterior Accessories','Exterior Vehicle Care','GPS','Hybrids','Interior Accessories','Interior Vehicle Care','Performance Parts & Accessories','SUVs','Sedans','Trucks','Wagons','Automatic','Imported Cars','ATVs & UTVs','Cruiser Bikes','Electric Bikes','Moto Batteries & Accessories','Moto Electronics','Moto Exterior Accessories','Moto Parts & Spares','Moto Tires & Wheels','Moto Tools & Maintenance','Moto oils & Fluids','Offroad Bikes','Riding Gear','Scooters','Sportbikes','Standard Bikes','Underbone'],
          "Pet Supplies": ['Cages & Accessories','Food','Grooming & Health','Beds & Feeding Accessories','Beds, Mats & Houses','Bowls & Feeders','Carriers & Travel','Cat Food','Cat Toys','Cat Treats','Clothing, Shoes & Accessories','Collars & Harnesses','Dental & Healthcare','Grooming','Health Supplies','Leashes & Collars','Litter & Toilet','Cages, Crates & Doors','Clean up & Toilet','Dog Flea & Tick','Dog Food','Dog Toys','Dog Treats','Leashes Collars & Muzzles','Training Aids','Aquariums Accessories','Aquariums, Tanks & Bowls','Habitats & Accessories'],
          "Sports & Outdoors": ['Headbands','Supports & Braces','Gloves','Martial Art Equipment','Protective Gear','Punching Bags & Accessories','Cardio Equipment','Fitness Accessories','Pilates','Running','Strength Training Equipment','Weight','Yoga','International Football Clubs','Pool, Darts & Foosball','Camping & Hiking','Climbing','Cycling','Fishing','Golf','Inline & Roller Skates','Shooting','Skateboards','Badminton','Squash','Table Tennis','Tennis','Boys','Girls','Men','Unisex','Women','Baseball','Basketball','Cricket','Football','Gymnastics','Hockey','Rugby','Sepak Takraw','Volleyball','Accessories','Swimming'],
          "Stationery & Craft": ['Accessories','Clothing','Shoes','Accessories','Ethnic Wear','Muslim Wear','Shoes','Lingerie, Sleep & Lounge'],
          "Tools, DIY & Outdoor": ['Safety Gloves','Work Jackets & Outerware','Door hardware & locks','Household Security Systems','Security Safes','Rechargeable & Flashlights'],
          "Toys & Games": ['Collectibles','Video Game Characters','Beads','Blackboards & Whiteboards','Clay & Dough','Craft Kits','Activity Gym & Playmats','Balls','Bath Toys','Crib Toys & Attachments','Early Learning','Indoor Climbers & Play Structures','Music & Sound','Push & Pull Toys','Rattles','Rocking & Spring Ride-Ons','Building Sets','Doll Accessories','Dollhouse Accessories','Dollhouses','Dolls','Playsets','Beauty & Fashion','Costumes','Music Players & Karaoke','RC Figures & Robots','Tablets','Walkie Talkies','Basic & Life Skills Toys','Early Development Toys','Musical Instruments','Reading & Writing','Balloons','Party & Games Crafts','3-D Puzzles','Brain Teasers','Die-Cast Vehicles','Drones & Accessories','Helicopters','Play Trains & Railway Sets','Play Vehicles','RC Vehicles & Batteries','Slime Toys','Squishy Toys','Fidget Spinners & Cubes','Flying Toys','Lawn Games','Outdoor Toys','Play Sets & Playground Equipment','Play Tents & Tunnels','Sports Play','Swimming Pool & Water Toys','Toys Sports','Board Games','Card Games','Game Room Games'],
          "Watches Sunglasses Jewellery": ['Accessories','Eyeglasses','Sunglasses','Kids','Men','Women','Unisex']
          }


# Level 2 sub category

movies = {"Bags and Travel": ["Kids Bags","Travel","Unisex Bags","Women Bags"],
          "Bedding & Bath": ['Bath','Bedding'],
          "Computers & Laptops": ['Computer Accessories','Computer Accessories','Computer Components','Desktops Computers','Laptops','Network Components','PC Gaming','Printers & Accessories','Scanners','Software','Storage'],
          "Cameras": ['Bridge','Camera Accessories','Car Cameras','DSLR','Drones','Gadgets & Other Cameras','Instant Camera','Lenses','Mirrorless','Optics','Point & Shoot','Security Cameras & Systems','Video & Action Camcorder',],
          "Digital Goods": ['Daraz Gift Cards','Financial Services','Games Gift Cards & Software','Home Services','Local Vouchers','Mobile Vouchers','Seller Services'],
          "Fashion": ['Boys', 'Girls','Kids','Men','Unisex','Women'],
          "Furniture & Dacor": ['Furniture','Home Dacor','Lighting','Storage & Organisation'],
          "Groceries": ['Bakery','Baking & Cooking','Beverages','Breakfast','Candy & Chocolate','Canned, Dry & Packaged Foods','Cigars & Cigarettes','Dairy & Chilled','Fresh Produce','Frozen','Gourmet Food and Gifts','Laundry & Household','Snacks','Tobacco','Wines, Beers & Spirits'],
          "Health & Beauty": ['Bath & Body','Beauty Tools','Food Supplements','Fragrances','Gift Sets','Hair Care','Makeup','Medical Supplies','Mens Care','Over The Counter Medicine','Over The Counter Medicine','Personal Care','Personal Pleasure','Services','Sexual Wellness','Skin Care'],
          "Home Appliances": ['Appliances Parts & Accessories','Cooling & Heating','Irons & Garment Steamers','Kitchen Appliances','Large Appliances','Sewing Machines','Small Kitchen Appliances','Vacuums & Floor Care','Washers & Dryers'],
          "Kitchen & Dining": ['Bakeware','Coffee & Tea','Cookware','Dinnerware','Drinkware','Kitchen & Table Linen','Kitchen Storage & Accessories','Kitchen Storage & Accessories','Kitchen Utensils','Serveware'],
          "Laundry & Cleaning": ['Cleaning','Laundry'],
          "Media, Music & Books": ['Books','Magazines','Magazines','Movies','Music','Musical Instruments','TV Series','eBooks'],
          "Mobiles & Tablets": ['Landline Phones','Mobile Accessories','Mobiles','Tablet Accessories','Tablets'],
          "Mother & Baby": ['Baby Gear','Baby Health Care','Baby Personal Care','Baby Safety','Clothing & Accessories','Diapering & Potty','Feeding','Gifts','Maternity Care','Nursery','Pacifiers & Accessories'],
          "Motors": ['Automotive','Cars','Motorcycle'],
          "Pet Supplies": ['Bird','Cat','Dog','Fish','Others','Small Pet'],
          "Sports & Outdoors": ['Accessories','Boxing, Martial Arts & MMA','Exercise & Fitness','Fan Shop','Games','Outdoor Recreation','Racket Sports','Shoes & Clothing','Shoes & Clothing','Team Sports','Water Sports'],
          "Stationery & Craft": ['Art Supplies','Craft Supplies','Gifts & Wrapping','Packaging & Cartons','Paper Products'],
          "Tools, DIY & Outdoor": ['Protective Clothing & Equipment','Security','Tool Storage & Shelving','Work Lights'],
          "Toys & Games": ['Action Figures & Collectibles','Arts & Crafts for Kids','Baby & Toddler Toys','Ball Pits & Accessories','Blocks & Building Toys','Dolls & Accessories','Dress Up & Pretend Play','Electronic Toys','Learning & Education','Party Supplies','Puzzle','Remote Control & Play Vehicles','Slime & Squishy Toys','Sports & Outdoor Play','Stuffed Toys','Traditional Games'],
          "Watches Sunglasses Jewellery": ['Eyewear','Jewellery','Watches']
          }


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('User Info for L2 & L3')
        self.createWidgets()
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=1, column=1, columnspan=100, padx=10, pady=10 ,sticky='ew')

    def updateMovies(self, event=None):
        self.movieCombo['values'] = movies[self.genreCombo.get()]
        self.movieCombo1['values'] = movies1[self.genreCombo.get()]
        Listbox1 = []
        Listbox2 = []
        for item in self.movieCombo['values']:
            self.Listbox1.insert('end', item)
        for item1 in self.movieCombo1['values']:
            self.Listbox2.insert('end', item1)

    def createWidgets(self):
        headingLabel = tk.Label(self, text="User Info for L2 & L3", font="Roboto 12 bold")
        headingLabel.grid(row=0, column=2, columnspan=5, padx=10, pady=10, sticky="w")


        tk.Label(self, text="SELECT START DATE", font="Roboto 8 bold").grid(row=2, column=1, padx=(5,0))
        self.cal1 = Calendar(font="Arial 14", selectmode='day',cursor="hand1", year=2020, month=1, day=1)
        self.cal1.bind('<<ComboboxSelected>>')
        self.cal1.grid(row= 3, column = 1,padx=10, pady=10)

        tk.Label(self, text="SELECT END DATE", font="Roboto 8 bold").grid(row=2, column=3, padx=(5,0))
        self.cal2 = Calendar(font="Arial 14", selectmode='day',cursor="hand1", year=2020, month=1, day=1)
        self.cal2.bind('<<ComboboxSelected>>')
        self.cal2.grid(row= 3, column = 3, padx=10, pady=10)

        tk.Label(self, text="SELECT CATEGORY 1", font="Roboto 8 bold").grid(row=5, column=1, padx=(5))
        self.genreCombo = tkinter.ttk.Combobox(self, width=30, values=list(movies.keys()), state="readonly")
        self.genreCombo.set("SELECT")
        self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        self.genreCombo.grid(row=6, column=1, padx=10, pady=10 )    

        tk.Label(self, text="SELECT CATEGORY 2", font="Roboto 8 bold").grid(row=5, column=2, padx=(5,0))
        self.movieCombo = tkinter.ttk.Combobox(width=30, state="readonly")
        self.movieCombo.bind('<<ComboboxSelected>>')
        self.movieCombo.set("SELECT")
        

        tk.Label(self, text="SELECT CATEGORY 3", font="Roboto 8 bold").grid(row=5, column=3, padx=(5,0))
        self.movieCombo1 = tkinter.ttk.Combobox( width=30, state="readonly")
        self.movieCombo1.bind('<<ComboboxSelected>>')
        self.movieCombo1.set("SELECT")
        

        self.Listbox1 =  tkinter.Listbox(self,activestyle='dotbox', selectbackground='blue', selectborderwidth=1,height=10,width=30,selectmode = 'multiple', exportselection=0)
        self.Listbox1.grid(row=6, column=2, padx=(0, 10))

        self.Listbox2 =  tkinter.Listbox(self,activestyle='dotbox', selectbackground='blue', selectborderwidth=1,height=10,width=30,selectmode = 'multiple', exportselection=0)
        self.Listbox2.grid(row=6, column=3, padx=(0, 10))

        self.Execute_button = tkinter.ttk.Button(text="Execute", width=30, command=self.createTimeButtons)
        self.Execute_button.grid(row=9, column=2, padx=(0, 10))

        tk.Label(self, text="Enter File Name", font="Roboto 8 bold").grid(row=8, column=1, padx=10, pady=10)
        self.file_name = tkinter.ttk.Entry(width = 30, state="writeonly")
        self.file_name.grid(row=8, column=2, padx=10, pady=10)

        self.Execute_button = tkinter.ttk.Button(text="Reset", width=30, command=self.resetbutton)
        self.Execute_button.grid(row=9, column=3, padx=(0, 5))


        tk.Label(self, text="** Categoy L3 must be selected according to category L2 & category L1 selection", font="Roboto 11 bold", foreground="red").grid(row=10, column=1, padx=20, pady=20)
        

        tkinter.ttk.Separator(self, orient="horizontal").grid(row=11, column=1, columnspan=100, padx=10, pady=10 ,sticky='ew')


    def resetbutton(self, event = None):
        # self.cal1.insert(0, x)
        # self.cal2.insert(0, x)
        self.genreCombo.set('SELECT')
        self.Listbox1.delete(0, 'end')
        self.Listbox2.delete(0, 'end')
        self.file_name.delete(0, 'end')

    def createTimeButtons(self, event=None):
        start_date_select = self.cal1.selection_get().strftime("%Y%m%d")
        end_date_select = self.cal2.selection_get().strftime("%Y%m%d")
        cat1_select = self.genreCombo.get()
        cat2_select = [self.Listbox1.get(v) for v in self.Listbox1.curselection()]
        cat3_select = [self.Listbox2.get(a) for a in self.Listbox2.curselection()]
        file_name = str(self.file_name.get())
       
        print(start_date_select)
        print(end_date_select)
        print(cat1_select)
        print(cat2_select)
        print(cat3_select)
        print(file_name)
       
        # Web Hooks

        o = ODPS('','','', endpoint='')
        options.tunnel.endpoint = '**API URL**'
        query="""SELECT  DISTINCT buyer_id
                        ,email_address
                        ,phone_number
                        ,venture_category1_name_en
                        ,venture_category2_name_en
                        ,venture_category3_name_en
                  FROM   Table Name AS t
                  WHERE  venture = ""
                  AND    order_status_esm NOT IN ('invalid')
                  AND    category1_name_en in ('"""+cat1_select+"""')
                  AND    category2_name_en in ("""+"'" + "','".join(cat2_select) + "'"+""")
                  AND    category3_name_en in ("""+"'" + "','".join(cat3_select) + "'"+""")
                  AND    TO_CHAR(t.order_create_date,'yyyymmdd') BETWEEN '"""+start_date_select+"""'
                  AND    '"""+end_date_select+"""'
                  """
        # Executing the query and set the data into a dataframe
        df = o.execute_sql(query).open_reader().to_result_frame().to_pandas()
        df.columns= df.columns.str.upper()
        date_string= arrow.now().format('YYYYMMDD')+' '+file_name
        df.to_csv(str(str(date_string)+'.csv'),index=False)
        print(query)

        

app = Application()
app.mainloop()