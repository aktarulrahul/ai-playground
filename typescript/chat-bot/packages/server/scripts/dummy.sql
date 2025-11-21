INSERT INTO products (id, name, description, price) VALUES
(1, 'Aurora Noise-Cancelling Headphones', 'Wireless over-ear headphones with adaptive noise control', 199.99),
(2, 'BrewMaster Pro Coffee Maker', '12-cup programmable coffee maker with built-in grinder', 149.50),
(3, 'FlexiFit Smartwatch X2', 'Lightweight smartwatch with health tracking and GPS', 249.00),
(4, 'PureMist Air Purifier 3000', 'HEPA air purifier suitable for medium-sized rooms', 179.90),
(5, 'UltraGlow Desk Lamp', 'LED desk lamp with adjustable brightness and color temperature', 59.99);

INSERT INTO reviews (author, rating, content, "productId", "createdAt") VALUES
('Emily R.', 5, 'These headphones completely transformed my commute. The noise cancellation is incredibly effective, blocking out train noise and chatter effortlessly. The sound quality feels rich with deep bass, and I can wear them for hours without discomfort thanks to the soft ear cushions.', 1, NOW()),
('Michael T.', 4, 'I bought these for office use and they have been fantastic for staying focused. Music sounds crisp and calls are clear, but I do wish the battery lasted slightly longer during long workdays.', 1, NOW()),
('Sarah L.', 5, 'The best wireless headphones I have owned. They connect instantly to my devices and the noise control adapts perfectly when I move between quiet and noisy environments. Great build quality too.', 1, NOW()),
('Jason P.', 4, 'Comfortable and stylish. The audio is impressive for both music and podcasts. They could fold a bit more compactly for travel, but overall an excellent purchase.', 1, NOW()),
('Ariana F.', 5, 'I use these daily at the gym and home. The noise cancellation helps me concentrate while working out, and the sound profile suits all genres. Absolutely worth the price.', 1, NOW()),

('Thomas W.', 5, 'This coffee maker has completely upgraded my mornings. The built-in grinder produces fresh grounds that make a noticeable difference in flavor. The programmable timer ensures a hot pot is ready when I wake up.', 2, NOW()),
('Linda G.', 4, 'Brews rich, smooth coffee and the machine is easy to clean. I love the aroma setting, though the grinder can be a bit loud early in the morning.', 2, NOW()),
('Robert C.', 5, 'Fantastic quality for the price. The coffee tastes café-level smooth and the machine warms quickly. A great choice for anyone who enjoys freshly ground beans.', 2, NOW()),
('Nina S.', 4, 'Makes consistently delicious coffee. The interface is simple and intuitive, though I wish the water reservoir were slightly larger for bigger households.', 2, NOW()),
('Olivia M.', 5, 'Great machine! The grinder works flawlessly and the brew strength options let me customize every cup. Highly recommend for serious coffee lovers.', 2, NOW()),

('Patrick D.', 5, 'The FlexiFit X2 is incredibly lightweight and the fitness tracking feels very accurate. GPS locks on quickly during outdoor runs and the heart-rate monitor has been spot-on.', 3, NOW()),
('Kelly H.', 4, 'Great smartwatch for daily use. Notifications come through instantly and the sleep tracking has helped me improve my schedule. Battery life could be a bit longer.', 3, NOW()),
('Daniel K.', 5, 'Excellent build quality and responsive interface. The health features are reliable and the workout modes cover everything I need. A perfect balance of function and comfort.', 3, NOW()),
('Maya R.', 4, 'I love the minimalist design and the comfort of wearing it all day. The step tracking and GPS accuracy are great, though the app could use a few more customization options.', 3, NOW()),
('Sophia P.', 5, 'The smartwatch works flawlessly for fitness tracking, notifications, and music control. It feels premium and the strap is very comfortable during long workouts.', 3, NOW()),

('James B.', 5, 'The PureMist Air Purifier has made a remarkable difference in my bedroom air quality. Dust and odors have decreased significantly, and my allergies are noticeably better.', 4, NOW()),
('Hannah U.', 4, 'Runs quietly and effectively cleans the air in my workspace. After a week of use, the room feels fresher and I’m breathing easier throughout the day.', 4, NOW()),
('Vincent L.', 5, 'Excellent filtration power for its size. The HEPA filter pulls out dust and fine particles, and I noticed improvements within 24 hours.', 4, NOW()),
('Rachel D.', 4, 'The purifier is sleek and quiet. Airflow is strong on higher settings and it has helped reduce pet hair and dander in my living room.', 4, NOW()),
('Eleanor J.', 5, 'A powerful and reliable air purifier. The automatic mode adjusts perfectly based on air quality, and the filter indicator is a great touch.', 4, NOW()),

('Chris A.', 5, 'This lamp provides beautifully even lighting and the adjustable brightness levels are perfect for long study sessions. The color temperature settings make it easy on the eyes at night.', 5, NOW()),
('Megan S.', 4, 'Stylish and functional. I love using this for my home office. The hinge adjusts smoothly and the different tones of light help reduce eye strain.', 5, NOW()),
('Alex P.', 5, 'A fantastic desk lamp for work and reading. The LEDs are bright but soft, and the touch controls are very responsive. Great value.', 5, NOW()),
('Jasmine Y.', 4, 'Good build quality and the light spread is excellent. I use it for drawing and the adjustable warmth helps with color accuracy.', 5, NOW()),
('Oliver G.', 5, 'Exactly what I needed for my desk setup. The lamp offers a wide range of brightness levels, and the minimalist design fits perfectly with my workspace.', 5, NOW());
