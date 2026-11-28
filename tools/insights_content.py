# Insights: short articles that each answer one question a furniture buyer asks.
# Block types: ("h3", text) ("p", text) ("ul", [items]) ("ol", [items]).
# Links: [[p:4|text]] product, [[page:guide|text]] page, [[cat:bedroom|text]] category page, [[art:slug|text]] another article.
# Rules: no invented facts, numbers about customers, delivery times or guarantees. Material notes are general information.

HUB_INTRO = [
    "Short, plain articles on the questions people ask before they order furniture: how to measure, which wood to pick, how big a sofa should be, what furniture costs, and how to look after what you buy.",
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
        "title": "Sheesham, Kikar or Deodar: Which Wood?",
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
        "title": "Plywood, MDF or Solid Wood: Which?",
        "meta": "How plywood, MDF and solid wood differ, and which one suits a wardrobe, a bed, a dining table or a bookshelf. Ask us if you are unsure.",
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
        "title": "Wooden Furniture Care in Humid Weather",
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
        "meta": "How to plan hanging space, shelves and drawers inside a wardrobe, starting from what you actually store. Send us your wall size for a price.",
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

NEW_ARTICLES = [
    {
        "slug": "furniture-prices-in-pakistan-explained",
        "title": "Furniture Prices in Pakistan Explained",
        "meta": "What decides the price of furniture in Pakistan: material, size, finish, fabric and labour. See our starting prices and how to compare two quotes.",
        "h1": "Furniture prices in Pakistan: what decides the cost",
        "short": "The price comes from the material, the size, the finish and the hours of work. Two quotes only compare when all four match.",
        "sections": [
            ("Why two prices for the same piece can differ", [
                ("p", "A quote for \"a wardrobe\" tells you little. One wardrobe may be 150 cm wide in board with a laminate finish. Another may be 210 cm wide with a solid wood frame and a polished finish. Both are wardrobes, and the prices will be far apart."),
                ("p", "So before you compare prices, compare what the price includes."),
            ]),
            ("What moves the price", [
                ("ul", [
                    "Material. Solid wood usually costs more than plywood. Plywood usually costs more than MDF or particle board. Read [[art:plywood-mdf-or-solid-wood|plywood, MDF or solid wood]] for what each is good at.",
                    "Size. A wider, taller or deeper piece uses more material and takes more hours to build.",
                    "Finish. Natural polish, paint, veneer and laminate cost different amounts, and a finish with several coats takes longer.",
                    "Fittings. Hinges, drawer runners, sliding tracks and handles range from basic to heavy duty.",
                    "Fabric and foam. For sofas and bed headboards, the cover and the foam inside change the price as much as the frame does.",
                    "Detail. Extra drawers, shelves, mirrors, carving or lighting add work.",
                ]),
            ]),
            ("Our starting prices", [
                ("p", "These are the starting prices shown on our product pages. Each one is for the standard size. The final price depends on your size and finish, and we confirm it before anything is built."),
                ("ul", [
                    "[[p:1|Dining table, 6 seater]]: from {price:1} ({spec:1})",
                    "[[p:2|Double bed with storage]]: from {price:2}",
                    "[[p:3|Wardrobe, 3 door]]: from {price:3}",
                    "[[p:4|Sofa set, 5 seater]]: from {price:4}",
                    "[[p:5|Office desk]]: from {price:5}",
                    "[[p:6|TV unit with shelves]]: from {price:6}",
                    "[[p:7|Coffee table]]: from {price:7}",
                    "[[p:8|Dressing table with mirror]]: from {price:8}",
                    "[[p:9|Bookshelf, 5 shelf]]: from {price:9}",
                ]),
            ]),
            ("How to compare two quotes", [
                ("ol", [
                    "Ask for the exact size in centimetres, and check it is the same in both quotes.",
                    "Ask what the frame, the back panel, the shelves and the drawer bottoms are made of.",
                    "Ask what finish is used and how many coats.",
                    "Ask what is included: delivery, fitting, chairs with a table, a mattress with a bed.",
                    "Ask when the work will be ready and when each payment is due.",
                ]),
                ("p", "If one quote cannot answer these, it is not yet a price you can compare."),
            ]),
            ("Ways to lower the cost without weakening the piece", [
                ("ul", [
                    "Choose a simpler finish. A plain finish costs less than a multi-coat one.",
                    "Make the piece the size you need, not larger. Measure the room first with [[art:measure-a-room-for-furniture|this guide]].",
                    "Use solid wood where the piece carries weight, such as legs and frames, and board for panels that carry none.",
                    "Cut the number of drawers or shelves you will not use.",
                ]),
            ]),
            ("Get a price for your size", [
                ("p", "Send the piece you want, the size and the finish on WhatsApp {PHONE}. We reply with a price. Nothing starts until you say yes."),
            ]),
        ],
        "faq": [
            ("Is solid wood always better than board?", "No. Solid wood is strong and can be repaired, but it moves with the weather. Good board stays flat and suits large panels. Many pieces use both."),
            ("Why is a made-to-order price different from a shop price?", "A shop price is for a fixed size and finish. A made-to-order price is for your size and your choices, so it can be lower or higher."),
            ("Can I get a price before I decide?", "Yes. Send your size and finish on WhatsApp and we reply with a price. You decide after that."),
        ],
        "links": [("p", 4), ("p", 2), ("p", 1), ("page", "shop"), ("page", "guide")],
    },
    {
        "slug": "wardrobe-design-for-a-small-room",
        "title": "Wardrobe Design for a Small Room",
        "meta": "Wardrobe design for a small bedroom: use the height, choose the right doors, keep the depth sensible and send the sizes we need for a price.",
        "h1": "Wardrobe design for a small room: what works",
        "short": "In a small room, build tall, keep doors from swinging into the walkway, and plan the inside before you choose the outside.",
        "sections": [
            ("Start with what you store", [
                ("p", "Count what you hang and what you fold. A wardrobe full of long coats needs a different inside from one holding folded shirts and bedding. [[art:plan-the-inside-of-a-wardrobe|Plan the inside first]], then fit the outside to the wall."),
            ]),
            ("Use the height", [
                ("p", "A wardrobe that runs close to the ceiling gives the most storage for the floor it takes. Put things you use a few times a year on the top shelf: bedding, suitcases, winter quilts. Measure the ceiling height at both ends of the wall, as in [[art:measure-a-room-for-furniture|how to measure a room]]."),
            ]),
            ("Choose doors that suit the space", [
                ("ul", [
                    "Hinged doors swing out, so they need clear floor about as wide as one door.",
                    "Sliding doors need no room in front, but only part of the wardrobe is open at one time.",
                    "Narrower hinged doors swing less, which helps when the bed stands close.",
                ]),
                ("p", "[[art:sliding-or-hinged-wardrobe-doors|Sliding or hinged wardrobe doors]] compares the two in more detail."),
            ]),
            ("Keep the depth sensible", [
                ("p", "Clothes on hangers need about 55 to 60 cm of depth. Folded clothes and shelves need less. A deeper wardrobe takes floor space you may not have, so put the hanging section at full depth and use shallower shelves beside it."),
            ]),
            ("Use corners and odd spaces", [
                ("p", "Alcoves, corners and the wall above a door can hold storage that a ready-made wardrobe cannot use. A wardrobe made to order can be cut to fit around a window, a beam or a recess. Send a photo with your numbers."),
            ]),
            ("Light colours and a mirror", [
                ("p", "A light finish makes a small room feel larger. A mirror on one door saves you buying a separate mirror and the floor space it needs."),
            ]),
            ("What to send us", [
                ("p", "Send the wall width, the ceiling height, the position of doors, windows and sockets, and a photo of the wall. Add what you store. We reply with questions or a price."),
            ]),
        ],
        "faq": [
            ("How wide should a wardrobe be for one person?", "As a rough guide, about 100 to 120 cm works for one person who mostly hangs clothes. Two people, or anyone with many long garments, will want 180 cm or more."),
            ("Can a wardrobe fit around a window or a beam?", "Yes. A made-to-order wardrobe can be cut around obstacles. Send the numbers and a photo."),
            ("Is a built-in wardrobe better for a small room?", "It often is, because it uses the full height and fills the corners. It is also harder to move later, so measure carefully and be sure of the position."),
        ],
        "links": [("p", 3), ("cat", "storage"), ("page", "custom")],
    },
    {
        "slug": "sliding-or-hinged-wardrobe-doors",
        "title": "Sliding or Hinged Wardrobe Doors?",
        "meta": "Sliding or hinged wardrobe doors? A plain comparison of space needed, access, wear and care, so you can pick the one that suits your bedroom.",
        "h1": "Sliding or hinged wardrobe doors: which should you choose?",
        "short": "Hinged doors open the whole wardrobe but need room to swing. Sliding doors need no swing space, but only open part of it at a time.",
        "sections": [
            ("Hinged doors", [
                ("ul", [
                    "You see the whole wardrobe at once, so it is easy to find things.",
                    "They need clear floor in front, about the width of one door.",
                    "Hinges are simple parts and are easy to adjust or replace.",
                    "A heavy mirror on a hinged door puts weight on the hinges, so the fitting must be chosen for it.",
                ]),
            ]),
            ("Sliding doors", [
                ("ul", [
                    "They need no space in front, which helps in a narrow room or when the bed is close.",
                    "Only part of the wardrobe is open at any time.",
                    "The track collects dust and grit, so it needs a regular wipe.",
                    "How smoothly they run depends on the track and wheels, and on the wardrobe standing level.",
                ]),
            ]),
            ("How to decide", [
                ("ul", [
                    "If the room is tight, choose sliding.",
                    "If you want to see everything and have the floor space, choose hinged.",
                    "If the wardrobe is wide, sliding doors or several narrower hinged doors are easier than two huge doors.",
                    "If you want both, hinged doors over the hanging section and open shelves or drawers beside it.",
                ]),
            ]),
            ("Check the fittings", [
                ("p", "Whichever you pick, ask what hinges or tracks will be used. Cheap fittings are the part that fails first. This matters most for tall doors and for doors with a mirror."),
            ]),
            ("Plan the whole wardrobe", [
                ("p", "The doors are one choice among several. Read [[art:wardrobe-design-for-a-small-room|wardrobe design for a small room]] and [[art:plan-the-inside-of-a-wardrobe|how to plan the inside]], then send us your sizes."),
            ]),
        ],
        "faq": [
            ("Which is cheaper, sliding or hinged?", "It depends on the size and the fittings, so ask for a quote for both. The difference is often in the hardware, not the door."),
            ("Do sliding doors jam?", "They can if dust fills the track or the wardrobe is not level. A regular wipe along the track and a level fitting prevent most problems."),
            ("Can I put a mirror on either type?", "Yes. A mirror is heavy, so the hinges or track should be chosen for that weight."),
        ],
        "links": [("p", 3), ("cat", "storage"), ("page", "custom")],
    },
    {
        "slug": "dining-table-size-by-seats",
        "title": "Dining Table Size by Number of Seats",
        "meta": "How big a dining table should be for 4, 6 or 8 people: space per person, room around the table, shapes and the sizes to send us for a price.",
        "h1": "Dining table size: how big for 4, 6 or 8 people",
        "short": "Allow about 60 cm of table edge for each person and about 90 cm behind each chair. Then test the size against your room.",
        "sections": [
            ("Start with the people", [
                ("p", "Each person needs roughly 60 cm of table edge to eat without bumping elbows. Here are rough sizes for a rectangular table:"),
                ("ul", [
                    "4 people: about 120 × 75 cm.",
                    "6 people: about 150 to 180 × 90 cm. Our [[p:1|6 seater dining table]] is {spec:1}.",
                    "8 people: about 200 to 240 × 90 to 100 cm.",
                ]),
                ("p", "These are guides, not rules. Chairs with arms need more room, and so do bigger families."),
            ]),
            ("Test it in your room", [
                ("ol", [
                    "Mark the table size on the floor with tape or sheets of newspaper.",
                    "Leave about 90 cm behind each chair so it can slide back.",
                    "If people walk behind the chairs, leave about 120 cm.",
                    "Stand where the door opens and check you can still get in and out.",
                ]),
                ("p", "[[art:measure-a-room-for-furniture|How to measure a room]] covers the rest of the numbers to write down."),
            ]),
            ("Choose the shape", [
                ("ul", [
                    "Rectangular tables seat the most people for the length.",
                    "A round table of about 100 to 120 cm suits four people in a square room, and no one sits in a corner.",
                    "In a long, narrow room, a narrower rectangular table leaves a better walking path.",
                ]),
            ]),
            ("Height and legs", [
                ("p", "Most dining tables stand about 74 to 76 cm high, and chairs with a seat around 45 cm high go with them. Look at where the legs are. Legs set at the corners leave more room for knees, and a leg set in from the end can block someone seated there."),
            ]),
            ("If you host a crowd only sometimes", [
                ("p", "Tell us how often you have a full table. A slightly longer table, or a separate side table for big days, can work better than a large table that fills the room every day."),
            ]),
        ],
        "faq": [
            ("How many people sit at a 180 × 90 cm table?", "Six, with three on each long side. Two more can sit at the ends if the legs allow it."),
            ("What size should dining chairs be?", "A seat about 45 cm from the floor suits a table about 75 cm high. That leaves roughly 28 to 30 cm between the seat and the tabletop."),
            ("Can the table be made to my size?", "Yes. Send the room size and how many people you seat, and we reply with a price."),
        ],
        "links": [("p", 1), ("cat", "dining"), ("page", "custom")],
    },
    {
        "slug": "bed-frame-size-and-your-mattress",
        "title": "Bed Frame Size and Your Mattress",
        "meta": "How to choose a bed frame size: measure the mattress, add the frame edge, leave room to walk and check storage and height before you order.",
        "h1": "Bed frame size: how to match the frame to your mattress",
        "short": "Decide the mattress first. The frame is the mattress size plus the edge around it, and the room needs space on every side you use.",
        "sections": [
            ("Measure the mattress, not the name", [
                ("p", "Names such as single, double, queen and king do not mean the same size at every brand. Measure the length, the width and the thickness of your mattress in centimetres. If you have not bought one yet, choose it first and send us its size."),
            ]),
            ("Add the frame", [
                ("ul", [
                    "The inside of the frame should match the mattress, with 1 to 2 cm of ease so the mattress goes in.",
                    "The outside is bigger by the thickness of the frame boards on every side.",
                    "A headboard adds depth at the head end, and a footboard adds length at the foot.",
                ]),
                ("p", "Always plan the room with the outside size, not the mattress size."),
            ]),
            ("Check the room", [
                ("ul", [
                    "About 60 cm beside the bed on each side you get in and out.",
                    "About 80 cm to walk past the foot of the bed.",
                    "Room for wardrobe doors and drawers to open.",
                    "Space for side tables if you want them.",
                ]),
            ]),
            ("If the bed has storage", [
                ("p", "Drawers need clear floor to pull out. A lift-up base needs room to reach the sides or the foot, and head room if a shelf sits above the bed. Tell us which kind you want and we plan the room around it. See the [[p:2|double bed with storage]]."),
            ]),
            ("Check the height", [
                ("p", "The mattress sits on the frame, so the height of the sleeping surface is the frame height plus the mattress thickness. A surface about 45 to 55 cm from the floor is comfortable for most adults to sit on and stand up from."),
            ]),
            ("What to send us", [
                ("p", "Send the mattress size and thickness, the room size, the position of the door and window, and whether you want storage. We reply with questions or a price."),
            ]),
        ],
        "faq": [
            ("Can you make a bed for a mattress I already have?", "Yes. Send the length, width and thickness of the mattress and we make the frame to match."),
            ("What if my room is small?", "Choose a low headboard, leave out the footboard, and check that the door and the wardrobe doors still open. Our article on wardrobe design for a small room has more ideas."),
            ("Should I buy the mattress or the bed first?", "The mattress. The frame is made around it, so its size decides the rest."),
        ],
        "links": [("p", 2), ("cat", "bedroom"), ("page", "custom")],
    },
]

# The price guide comes first because it answers the most searched question.
ARTICLES = NEW_ARTICLES[:1] + ARTICLES + NEW_ARTICLES[1:]
