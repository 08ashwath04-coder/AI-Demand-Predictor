from datetime import date
from app.database import SessionLocal,Base,engine
from app.models import Product,Crop,Inventory,CalendarEvent
Base.metadata.create_all(bind=engine);db=SessionLocal()
if not db.query(Product).count():
 products=[Product(name='Rice',category='Grains',description='Staple grain'),Product(name='Tomato',category='Vegetable',description='Fresh tomato'),Product(name='Onion',category='Vegetable',description='Fresh onion'),Product(name='Potato',category='Vegetable',description='Fresh potato'),Product(name='Banana',category='Fruit',description='Fresh banana')];db.add_all(products);db.flush();db.add_all([Inventory(product_id=1,current_stock=150,minimum_stock=100),Inventory(product_id=2,current_stock=80,minimum_stock=120),Inventory(product_id=3,current_stock=130,minimum_stock=100)])
if not db.query(Crop).count(): db.add_all([Crop(name='Rice',season='Kharif',category='Grain'),Crop(name='Tomato',season='Winter',category='Vegetable'),Crop(name='Onion',season='Winter',category='Vegetable'),Crop(name='Potato',season='Winter',category='Vegetable')])
if not db.query(CalendarEvent).count(): db.add_all([CalendarEvent(date=date(2026,1,14),title='Pongal',event_type='Festival',description='High seasonal food demand'),CalendarEvent(date=date(2026,4,14),title='Tamil New Year',event_type='Festival',description='Potential retail demand increase'),CalendarEvent(date=date(2026,8,15),title='Independence Day',event_type='Holiday',description='Potential retail activity increase'),CalendarEvent(date=date(2026,10,20),title='Festival Season',event_type='Demand',description='Potential grocery demand increase')])
db.commit();db.close();print('Seed complete')
