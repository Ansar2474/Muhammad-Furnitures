# Insights: short articles that each answer one question a furniture buyer asks.
# Block types: ("h3", text) ("p", text) ("ul", [items]) ("ol", [items]).
# Links: [[p:4|text]] product, [[page:guide|text]] page, [[cat:bedroom|text]] category page, [[art:slug|text]] another article.
# Rules: no invented facts, numbers about customers, delivery times or guarantees. Material notes are general information.

HUB_INTRO = [
    "Short, plain articles on the questions people ask before they order furniture: how to measure, which wood to pick, how big a sofa should be, and how to look after what you buy.",
    "Each one answers a single question. For a wider overview, read the [[page:guide|furniture buying guide]].",
]

ARTICLES = [
    {
        "slug": "measure-a-room-for-furniture",
        "title": "How to Measure a Room for Furniture",
        "meta": "A simple way to measure your room, doors and stairs before you order furniture, with the numbers to send for a made-to-order price.",
        "h1": "How to measure a room before you order furniture",
        "short": "Measure the space where the piece will stand, then the doors and stairs it must pass through. Write every number in centimetres and take a photo.",
        "sections": [
            ("What you need", [
                ("p", "A tape measure, a pen and your phone. Measure twice. A mistake of 3 cm is enough to make a wardrobe touch the ceiling or a bed block a door."),
            ]),
            ("Measure the space", [
                ("ol", [
                    "Width: measure the wall along the floor and again near the ceiling. Walls are often not straight, so use the smaller number.",
                    "Depth: measure from the wall to the point where the furniture should end. Keep the space in front free for walking.",
                    "Height: measure at both ends of the wall. Ceilings and floors are often uneven, and the lower number is the one that matters.",
                ]),
                ("p", "Note anything on the wall: sockets, switches, windows, an air conditioner or a skirting board. Furniture often has to work around them."),
            ]),
            ("Measure the way in", [
                ("p", "A piece that does not fit through the door never reaches the room. Measure the width of the front door, the room door, any narrow corridor and every turn on the stairs. Tell us whether there is a lift. Wardrobes and sofa sets are the pieces that most often get stuck, so tell us if the way in is tight and we talk through it before the piece is built."),
            ]),
            ("Leave room to use it", [
                ("ul", [
                    "About 80 cm of walking path between furniture.",
                    "About 60 cm beside a bed, on the side you get in and out.",
                    "About 90 cm behind dining chairs, so they can slide back.",
                    "Enough space in front of a wardrobe for the doors to open.",
                ]),
            ]),
            ("What to send us", [
                ("p", "Send the numbers and one or two photos of the wall on WhatsApp. For a bed, add your mattress size. A rough sketch with the numbers on it is enough. We reply with questions or a price, and we change the design if your measurements need it."),
            ]),
        ],
        "faq": [
            ("Should I measure in centimetres or feet?", "Either works, as long as you tell us which one. Centimetres are easier to add up and less likely to be misread."),
            ("What if my walls are not straight?", "Measure at the top, the middle and the bottom, and send the smallest number. Furniture can be made to follow an uneven wall if you tell us about it."),
        ],
        "links": [("p", 3), ("p", 2), ("page", "custom")],
    },
    {
        "slug": "sheesham-kikar-deodar-wood",
        "title": "Sheesham, Kikar and Deodar: Which Wood to Choose",
        "meta": "What sheesham, kikar and deodar are like to live with, and how to choose between them and between solid wood and board for your furniture.",
        "h1": "Sheesham, kikar and deodar: which wood for which piece",
        "short": "Sheesham is dense and polishes well. Kikar is hard and heavy. Deodar is lighter and softer. The right one depends on the piece, the room and your budget.",
        "sections": [
            ("Sheesham", [
                ("p", "Sheesham is a dense hardwood with a brown colour that ranges from golden to dark, and a clear grain. It is strong, takes a polish well, and can be sanded and polished again years later. It usually costs more than the other two. It suits pieces that take daily use, such as dining tables, bed frames and desks."),
            ]),
            ("Kikar", [
                ("p", "Kikar is also a hard, heavy wood. It is often used for frames, legs and solid pieces. Its grain is more uneven than sheesham, and it can have knots. Whether a kikar piece stays flat depends a great deal on how well the wood was dried before it was cut, so ask your maker about that."),
            ]),
            ("Deodar", [
                ("p", "Deodar is a softwood with a light colour and a pleasant smell. It is lighter than sheesham or kikar and easy to work. Because it is softer, it dents more easily. It is a common choice for doors, windows and simple furniture where weight and cost matter."),
            ]),
            ("Wood or board?", [
                ("p", "Many good pieces use both. A dining table top in solid wood, for example, and the inside of a wardrobe in plywood. The [[art:plywood-mdf-or-solid-wood|next article]] explains where each one makes sense."),
            ]),
            ("Questions to ask before you pay", [
                ("ul", [
                    "Which wood or board is used for each part of the piece?",
                    "How was the wood dried before it was cut?",
                    "What finish goes on it: natural polish, stain or paint?",
                    "Can I see the wood or a sample of the finish before you start?",
                ]),
                ("p", "A maker who has clear answers to these is worth talking to. We are happy to answer them for any piece we build."),
            ]),
        ],
        "faq": [
            ("Which wood is best for furniture?", "There is no single best wood. Sheesham is a strong and popular choice for pieces that get daily use. The right wood depends on the piece, the room and your budget."),
            ("Can I order a piece in a wood I choose?", "Yes. Tell us which wood you want or what your budget is, and we suggest options and price them."),
        ],
        "links": [("p", 1), ("p", 2), ("cat", "dining")],
    },
    {
        "slug": "plywood-mdf-or-solid-wood",
        "title": "Plywood, MDF or Solid Wood: What to Choose",
        "meta": "How plywood, MDF and solid wood differ, and which one suits a wardrobe, a bed, a dining table or a bookshelf.",
        "h1": "Plywood, MDF or solid wood: what to choose for each piece",
        "short": "Solid wood suits tables and bed frames. Plywood suits wardrobes and shelves. MDF suits painted surfaces, but keep it dry. Many pieces use more than one.",
        "sections": [
            ("Solid wood", [
                ("p", "Solid wood is cut from a plank of timber. It is heavy and strong, and it can be sanded and polished again later. It moves a little with the weather, so a good maker allows for that. It is the usual choice for table tops, bed frames and chair legs."),
            ]),
            ("Plywood", [
                ("p", "Plywood is made of thin layers of wood glued together, with the grain of each layer turned at right angles to the one before. That keeps it flat, so it suits wardrobe doors, cupboard sides and shelves. Quality varies a lot. It depends on the glue and the layers inside, so ask which grade is used."),
            ]),
            ("MDF", [
                ("p", "MDF is made of fine wood fibre pressed with glue. Its surface is smooth, so it takes paint well, and it is often used for painted doors and panels. It swells when it gets wet and holds screws less well than wood, so keep it away from damp walls and do not use it where water spills."),
            ]),
            ("Veneer and laminate", [
                ("p", "Veneer is a thin slice of real wood glued onto board, so you get the look of wood on a flat, stable base. Laminate is a printed plastic layer. It resists scratches and stains well, but it cannot be sanded and polished again."),
            ]),
            ("A simple guide", [
                ("ul", [
                    "Dining table: solid wood top, since it is used and cleaned every day.",
                    "Bed: solid wood frame, with a board base for the storage.",
                    "Wardrobe: plywood body for flat doors and sides, with a finish that suits your room.",
                    "Bookshelf: plywood or solid wood shelves, thick enough not to sag under books.",
                    "Painted TV unit or console: MDF or plywood, kept away from damp.",
                ]),
            ]),
        ],
        "faq": [
            ("Is plywood worse than solid wood?", "No. They do different jobs. Good plywood stays flatter than solid wood, which is why it suits wardrobes and shelves. Poor plywood is the problem, so ask which grade is used."),
            ("Can MDF furniture get wet?", "No. MDF swells when it gets wet, so keep it away from damp walls and spills."),
        ],
        "links": [("p", 3), ("p", 9), ("cat", "storage")],
    },
    {
        "slug": "how-big-should-a-sofa-set-be",
        "title": "How Big Should Your Sofa Set Be?",
        "meta": "How to choose the size of a sofa set for your living room, with the clearances to leave around it and what to tell a maker.",
        "h1": "How big should your sofa set be?",
        "short": "Measure the wall the sofa will stand against, leave about 80 cm to walk, and keep about 40 cm between the sofa and the centre table.",
        "sections": [
            ("Start with the wall", [
                ("p", "The longest wall in the room is usually where the three seater goes. A three seater is commonly around 180 to 210 cm long, and a single seater around 80 to 100 cm. A made-to-order set can be longer or shorter, so measure your wall and plan the rest around it."),
            ]),
            ("Leave room to move", [
                ("ul", [
                    "About 80 cm of walking path between the sofas and the other furniture.",
                    "About 40 cm between the sofa and the centre table.",
                    "Enough space to open the door and pass the sofa without turning sideways.",
                ]),
                ("p", "If the room is small, two pieces of the right size look better than a full set that fills it. A 3 + 1 set, or a three seater with a pair of chairs, is often enough."),
            ]),
            ("Think about how many people sit", [
                ("p", "Count how many people sit in the room on a normal evening, and how many sit when guests come. Plan for the normal evening and add chairs or a floor seat for guests. A sofa set that is too big for daily use makes the room feel crowded every day to serve a few days a year."),
            ]),
            ("The way in", [
                ("p", "Check the width of your front door and stairs. A sofa that is too wide to carry in is a problem you only find on delivery day. Tell us about the way in, and we talk through it before the piece is built."),
            ]),
            ("What to tell us", [
                ("p", "Send the wall length, the door width, a photo of the room and how many people usually sit. Add the fabric colour you have in mind. We suggest a size and send a price."),
            ]),
        ],
        "faq": [
            ("What is a 3 + 1 + 1 sofa set?", "It is one three seater and two single seaters. It is the set we list as our 5 seater sofa set."),
            ("Can you make a sofa set in my size?", "Yes. Send us your wall length and we plan the set to it."),
        ],
        "links": [("p", 4), ("p", 7), ("cat", "living")],
    },
    {
        "slug": "wooden-furniture-care-humid-weather",
        "title": "Looking After Wooden Furniture in Humid Weather",
        "meta": "Simple ways to protect wooden furniture in the monsoon and other humid weather: airflow, distance from walls, cleaning and spills.",
        "h1": "Looking after wooden furniture in humid weather",
        "short": "Keep air moving, leave a small gap between furniture and wet walls, wipe spills at once, and clean with a dry or slightly damp cloth.",
        "sections": [
            ("Why humidity matters", [
                ("p", "Wood takes in moisture from damp air and gives it back when the air dries. This is why doors can stick in the monsoon and loosen again in winter. You cannot stop it, but you can reduce the damage."),
            ]),
            ("What to do", [
                ("ul", [
                    "Leave a gap of a few centimetres between a wardrobe or bookshelf and an outside wall, so air can move behind it.",
                    "Open windows on dry days. Close them when it rains, if water comes in.",
                    "Keep furniture off wet floors. After mopping, wait for the floor to dry before you slide pieces back.",
                    "Do not put damp clothes or towels in a wardrobe.",
                    "Fix tall shelves to the wall, so a loosened frame cannot tip.",
                ]),
            ]),
            ("Cleaning", [
                ("p", "Dust with a soft dry cloth. For marks, use a cloth wrung out until it is only slightly damp, and dry the surface straight away. Strong cleaners can dull a polished top, so avoid them. Use mats and coasters under hot dishes and cups."),
            ]),
            ("If you see a problem", [
                ("p", "Small white or grey marks on a surface often come from moisture or heat and may fade with time. A door that sticks usually frees itself when the weather dries. If you see mould, black patches or a frame that has bent, message us a photo and we tell you what we would do."),
            ]),
        ],
        "faq": [
            ("Should I polish furniture during the monsoon?", "It is better to wait for dry weather. A polish applied in damp air can dry cloudy."),
            ("Can I put a wardrobe against an outside wall?", "Yes, but leave a small gap behind it so air can move, because outside walls are often the dampest in the house."),
        ],
        "links": [("p", 3), ("p", 1), ("page", "guide")],
    },
    {
        "slug": "made-to-order-or-ready-made-furniture",
        "title": "Made-to-Order or Ready-Made Furniture?",
        "meta": "An honest comparison of made-to-order and ready-made furniture: fit, price, waiting time and what to check before you decide.",
        "h1": "Made-to-order or ready-made furniture: which one should you buy?",
        "short": "Ready-made is faster and lets you see the piece first. Made-to-order fits your room and your choices better. Pick by how much your room needs a particular size.",
        "sections": [
            ("What ready-made gives you", [
                ("ul", [
                    "You see the real piece before you buy.",
                    "You can usually take it home sooner.",
                    "The price is fixed and easy to compare.",
                ]),
                ("p", "Ready-made is a good choice when your room suits standard sizes and you are not choosing a particular colour or finish."),
            ]),
            ("What made-to-order gives you", [
                ("ul", [
                    "A size that fits your wall, your mattress or your door.",
                    "Your choice of wood or board, fabric, colour and finish.",
                    "Details you can ask for, such as drawers in a desk or the layout inside a wardrobe.",
                ]),
                ("p", "It suits rooms with an unusual shape, low ceilings, alcoves or a mattress that is not a standard size."),
            ]),
            ("What to check with made-to-order", [
                ("ol", [
                    "Ask for the price in writing, with the size, materials and finish named.",
                    "Ask how long the piece will take, and when you will be told if that changes.",
                    "Ask how payment works and when it is due.",
                    "Ask what happens if the piece does not match what was agreed.",
                ]),
                ("p", "Our standard is a price before any work starts, with the details in writing. See [[page:custom|how custom orders work]]."),
            ]),
            ("How to decide", [
                ("p", "If a standard size fits and you like what you see, ready-made is simple. If you have measured and the standard sizes leave gaps, or you want a finish you cannot find, made-to-order is worth the wait. Send us your room size and we tell you honestly whether you need a custom size at all."),
            ]),
        ],
        "faq": [
            ("Is made-to-order furniture more expensive?", "Not always. The price depends on size, materials and finish. We price the piece you describe, so you can compare it with a ready-made one."),
            ("Can I change an order after I place it?", "Tell us as early as you can. Changes made before work starts are easy, and the price changes with them."),
        ],
        "links": [("page", "custom"), ("page", "shop"), ("page", "contact")],
    },
    {
        "slug": "plan-the-inside-of-a-wardrobe",
        "title": "How to Plan the Inside of a Wardrobe",
        "meta": "How to plan hanging space, shelves and drawers inside a wardrobe, starting from what you actually store.",
        "h1": "How to plan the inside of a wardrobe",
        "short": "List what you store, measure your longest garment, and give each group its own space: hanging, folded, drawers and a shelf for bags and bedding.",
        "sections": [
            ("Start with what you own", [
                ("p", "Before you choose a design, make a rough list: how many long garments, how many shirts, how much folded clothing, bedding, bags and shoes. The inside of the wardrobe should follow that list, not a standard layout."),
            ]),
            ("Hanging space", [
                ("p", "Measure your longest garment on its hanger, then add about 10 cm so it does not touch the floor of the wardrobe. Long kameez, coats and wedding clothes need full height. Shirts and short kameez need about half, so one tall rail and one lower pair of rails can hold more than a single rail."),
            ]),
            ("Shelves and drawers", [
                ("ul", [
                    "Shelves about 35 to 40 cm apart suit folded clothes and keep stacks from getting too high.",
                    "Drawers suit small items such as socks, scarves and jewellery boxes.",
                    "A top shelf holds bedding, suitcases and things you use rarely.",
                    "A narrow section with shelves suits bags and belts.",
                ]),
            ]),
            ("Doors", [
                ("p", "Hinged doors need space in front of the wardrobe to open. If the room is tight, say so and we talk through the layout. A mirror on a door saves wall space in a small bedroom."),
            ]),
            ("What to send us", [
                ("p", "Send the wall width and height, a photo, and your list of what you store. We plan the inside with you and send a price. The standard [[p:3|3 door wardrobe]] is 150 × 60 × 210 cm and can be changed to fit."),
            ]),
        ],
        "faq": [
            ("How deep should a wardrobe be?", "About 55 to 60 cm suits clothes on hangers. Our standard 3 door wardrobe is 60 cm deep. Tell us if your space is shallower."),
            ("Can I have drawers inside the wardrobe?", "Yes. Tell us how many you want and what they will hold."),
        ],
        "links": [("p", 3), ("cat", "storage"), ("page", "guide")],
    },
]
