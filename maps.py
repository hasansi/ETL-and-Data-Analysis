mapping_street = { "St": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
	    "Rd":"Road",
            "St.": "Street",
	    "PARK": "Park",
	    "Blvd": "Boulevard",
            "PT": "Point",
	    "FLT": "Flat",
	    "Larue": "LaRue",
	    "RST": "Rest",
	    "Fritz1": "Summit At Fritz Farm",
	    "Kingston2": "Kingston Road",
	    "Kingswood": "Kingswood Drive",
	    "Vista": "Vista",
	    "Lake": "Lake",
	    "Bryanprop": "Bryanprop",
	    "Bryanprop": "Bryanprop",
	    "Ln": "Lane",
	    "Fritz3": "Summit At Fritz Farm",
	    "Fountain": "Fountain",
	    "Kingston1": "Kingston Road",
	    "Kingston3": "Kingston Road",
	    "Dominion": "Dominion",
	    "Bay": "Bay",
	    "Blvd.": "Boulevard",
	    "Manor": "Manor",
	    "Fritz2": "Summit At Fritz Farm",
	    "Esplanade": "Esplanade",
	    "Boardwalk": "Boardwalk",
	    "Close": "Close",
	    "Creek": "Creek",
	    "Ct": "Court",
	    "Dr": "Drive"
	  }

expected_street = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",            "Trail","Parkway","Commons","Ridge","Heights","Station","Hill","Way","End","Circle","#120","Crest","Meadows","Dale","Run","Garden",
"Trace","Farm","Park","Cove","Path","View","Champions","Retreat","Bend","Pike","Plaza","Green","Estates",
"Loop","Point","Spring","Alley","Walk","Terrace","Pass","Broadway","Row", "Glen", "Limestone","146","7", "Curtilage", "Wynd", 
"Bluff", "Knoll", "Calgary", "Maxima"]

mapping_amenity = {'toilets' : 'toilets',
		   'university' : 'university',
		   'veterinary' : 'veterinary',
		   'townhall' : 'townhall',
		   'public_building;courthouse' : 'courthouse',
		   'ATM' : 'atm',
		   'yes' : 'other',
		   'waste_basket' : 'waste_basket'}


expected_amenity = ['administration', 'advertising', 'alm', 'animal_boarding', 'animal_breeding', 'animal_shelter', 'architect_office', 'arts_centre', 'artwork', 'atm', 'audiologist', 'baby_hatch', 'baking_oven', 'bank', 'bar', 'bbq', 'bench', 'bicycle_parking', 'bicycle_rental', 'bicycle_repair_station', 'bicycle_trailer_sharing', 'biergarten', 'bikeshed', 'boat_rental', 'boat_sharing', 'boat_storage', 'brothel', 'bts', 'bureau_de_change', 'bus_station', 'cafe', 'canoe_hire', 'car_pooling', 'car_rental', 'car_repair', 'car_sharing', 'car_wash', 'casino', 'charging_station', 'childcare', 'cinema', 'citymap_post', 'clinic', 'clock', 'club', 'coast_guard', 'coast_radar_station', 'college', 'community_center', 'community_centre', 'compressed_air', 'concert_hall', 'conference_centre', 'courthouse', 'coworking_space', 'crematorium', 'crucifix', 'crypt', 'customs', 'dancing_school', 'dead_pub', 'dentist', 'disused', 'dive_centre', 'doctors', 'dog_bin', 'dog_waste_bin', 'dojo', 'drinking_water', 'driving_school', 'education', 'embassy', 'emergency_phone', 'emergency_service', 'events_venue', 'ev_charging', 'exhibition_centre', 'fast_food', 'feeding_place', 'ferry_terminal', 'festival_grounds', 'financial_advice', 'fire_hydrant', 'fire_station', 'first_aid', 'fish_spa', 'food_court', 'fountain', 'fuel', 'gambling', 'game_feeding', 'garages', 'grave_yard', 'grit_bin', 'gym', 'harbourmaster', 'hospice', 'hospital', 'hotel', 'hunting_stand', 'ice_cream', 'internet_cafe', 'jobcentre', 'kindergarten', 'kiosk', 'kitchen', 'Kneippbecken', 'kneipp_water_cure', 'language_school', 'lavoir', 'library', 'lifeboat_station', 'life_ring', 'loading_dock', 'love_hotel', 'marae', 'marketplace', 'milk_dispenser', 'mobile_library', 'monastery', 'money_transfer', 'mortuary', 'motorcycle_parking', 'motorcycle_rental', 'music_school', 'music_venue', 'nameplate', 'nightclub', 'nursery', 'nursing_home', 'park', 'parking', 'parking_entrance', 'parking_space', 'pharmacy', 'photo_booth', 'place_of_worship', 'planetarium', 'police', 'post_box', 'post_office', 'preschool', 'printer', 'prison', 'prison_camp', 'proposed', 'pub', 'public_bath', 'public_bookcase', 'public_building', 'public_hall', 'ranger_station', 'recycling', 'refugee_housing', 'register_office', 'rescue_box', 'rescue_station', 'research_institute', 'restaurant', 'retirement_home', 'sanatorium', 'sanitary_dump_station', 'sauna', 'school', 'scout_hut', 'shelter', 'shop', 'shower', 'ski_school', 'smoking_area', 'social_centre', 'social_facility', 'spa', 'stables', 'stripclub', 'studio', 'swimming_pool', 'swingerclub', 'table', 'taxi', 'telephone', 'theatre', 'ticket_booth', 'ticket_validator']

expected_shop = ['accessories', 'alcohol', 'anime', 'antique', 'antiques', 'art', 'auto_parts', 'baby_care', 'baby_goods', 'bag', 'bakery', 'bathroom_furnishing', 'beauty', 'bed', 'betting', 'beverages', 'bicycle', 'boat', 'bookmaker', 'books', 'boutique', 'brewing_supplies', 'business_machines', 'butcher', 'camera', 'candles', 'car', 'carpet', 'car_bodyshop', 'car_parts', 'car_repair', 'car_service', 'chandler', 'charity', 'cheese', 'chemist', 'chocolate', 'clothes', 'coffee', 'collector', 'computer', 'confectionery', 'convenience', 'copyshop', 'cosmetics', 'country_store', 'craft', 'curtain', 'dairy', 'deli', 'department_store', 'discount', 'dive', 'doityourself', 'dry_cleaning', 'e-cigarette', 'electrical', 'electronics', 'energy', 'erotic', 'estate_agent', 'fabric', 'farm', 'fashion', 'fireplace', 'fireworks', 'fish', 'fishing', 'fishmonger', 'flooring', 'florist', 'food', 'frame', 'free_flying', 'frozen_food', 'fuel', 'funeral_directors', 'furnace', 'furniture', 'gallery', 'gambling', 'games', 'garden_centre', 'garden_furniture', 'gas', 'general', 'gift', 'glass', 'glaziery', 'golf', 'greengrocer', 'grocery', 'haberdashery', 'hairdresser', 'hairdresser_supply', 'hardware', 'health', 'health_food', 'hearing_aids', 'herbalist', 'hifi', 'hobby', 'household', 'houseware', 'hunting', 'ice_cream', 'interior_decoration', 'jewellery', 'jewelry', 'junk_yard', 'kiosk', 'kitchen', 'lamps', 'laundry', 'leather', 'lighting', 'locksmith', 'lottery', 'mall', 'massage', 'medical', 'medical_supply', 'military_surplus', 'mobile_phone', 'model', 'moneylender', 'money_lender', 'motorcycle', 'motorcycle_repair', 'music', 'musical_instrument', 'newsagent', 'nutrition_supplements', 'office_supplies', 'optician', 'organic', 'outdoor', 'paint', 'party', 'pasta', 'pastry', 'pawnbroker', 'perfume', 'perfumery', 'pet', 'pharmacy', 'photo', 'photography', 'piercing', 'pottery', 'printing', 'pyrotechnics', 'radiotechnics', 'religion', 'rental', 'scuba_diving', 'seafood', 'second_hand', 'sewing', 'ship_chandler', 'shoes', 'shoe_repair', 'shopping_centre', 'solarium', 'souvenir', 'spare_parts', 'spices', 'sports', 'stationery', 'supermarket', 'swimming_pool', 'tailor', 'tattoo', 'tea', 'ticket', 'tickets', 'tiles', 'tobacco', 'toys', 'trade', 'travel_agency', 'trophy', 'tyres', 'vacant', 'vacuum_cleaner', 'variety_store', 'video', 'video_games', 'watches']

mapping_shop = {'yes' : 'other',
		'HVAC_Equipment' : 'hardware',
		'barber' : 'barber',
		'quilting' : 'beds'
}

expected_office = ['accountant', 'administrative', 'adoption_agency', 'advertising_agency', 'architect', 'association', 'charity', 'company', 'educational_institution', 'employment_agency', 'energy_supplier', 'estate_agent', 'financial', 'forestry', 'foundation', 'government', 'guide', 'insurance', 'it', 'lawyer', 'logistics', 'moving_company', 'newspaper', 'ngo', 'notary', 'occupational_safety', 'parish']

mapping_office = {'yes' : 'other',
		  'telecommunication' : 'telecommunication',
		  'therapist' : 'therapist',
		  'construction' : 'construction',
		  'non-profit' : 'non-profit'}

mapping_postcode = {'40542' : '40508',
		    '40347' : '40347',
		    '40356' : '40356',
		    '40390' : '40390',
		    '40379' : '40379',
		    '40361' : '40361',
		    '40536' : '40536',
		    '40324' : '40324',
		    '40504-3504' : '40504',
		    '40509-9071' : '40509',
		    '40383' : '40383',
		    'KY' : '40508',
		    '40503-1926' : '40503'}

expected_postcode = ['40502','40503','40504','40505','40506','40507','40508','40509','40510','40511','40512','40513','40514','40515','40516','40517']






