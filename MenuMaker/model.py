from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    thumbnail = Column(Text, nullable=True)
    item = relationship("Item", back_populates="category")
    
    def __repr__(self):
        return ("<Category(id = {}, name = {}, thumbnail = {})>".format(self.id, self.name, self.thumbnail))
    

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    thumbnail = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    category_id =  Column(Integer, ForeignKey('category.id'))
    
    category = relationship("Category", back_populates="item")
    
    def __repr__(self):
        return ("<Item(id = {}, name = {}, thumbnail = {}, price = {}, categoryId = {})>".format(self.id,self.name,self.thumbnail,self.price,self.category_id))



class Invoice(Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    itemlist = relationship("ItemList", order_by="ItemList.id", back_populates="invoice")
    #def __repr__(self):
    #    return ("<Invoice(id = {}, Amount = {})>".format(self.id, self.amount))
   
class ItemList(Base):
    __tablename__ = 'itemlist'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    
    invoice = relationship("Invoice", back_populates="itemlist")
    
    #def __repr__(self):
    #    return ("<ItemList(id = {}, InvoiceId = {}, ItemId = {}, Quantity = {}, Amount = {})>".format(self.id, self.invoice_id, self.item_id, self.quantity, self.amount))
    

engine = create_engine('sqlite:///menuMaker.db')
session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
