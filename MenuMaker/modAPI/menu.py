# Import the database object from the database model module
from MenuMaker.model import Category, Item
from flask import url_for

class Menu():
    def __init__(self, session):
        #self.category = Category()
        #self.item = Item()
        self.session = session
        self.query = self.session.query
    
    def makeItemBean(self,item):
        newItem = {}
        for field in item:
            if field == 'id':
                newItem['uri'] = url_for('api.getMenuItem', menu_id = item['id'], _external = True)
            else:
                newItem[field] = item[field]
        return newItem
        
    def makeCategoryBean(self,category):
        newCat = {}
        for field in category:
            if field == 'id':
                newCat['uri'] = url_for('api.getCatItem', cat_id = category['id'], _external = True)
            else:
                newCat[field] = category[field]
        return newCat
    
        
    def getMenuList(self):
        tmpList = []
        
        for instance in self.query(Category).order_by(Category.id):
            itemList = []
            for inst in self.query(Item).filter(Item.category_id == instance.id).all() :
                temp = dict(id = inst.id, name = inst.name, thumbnail = inst.thumbnail, price = inst.price)
                itemList.append(temp)
            #print(instance)
            temp = dict(id = instance.id, name = instance.name, thumbnail = instance.thumbnail, items = list(map(self.makeItemBean, itemList)) )
            tmpList.append(temp)
        
        menuList = {"menu" : dict(category = tmpList) }
        return menuList
            
    def getCategoryList(self):
        tmpList = []
        
        for instance in self.query(Category).order_by(Category.id):
            #print(instance)
            temp = dict(id = instance.id, name = instance.name, thumbnail = instance.thumbnail)
            tmpList.append(temp)
        
        categoryList = dict(category = list(map(self.makeCategoryBean, tmpList)))
        return categoryList
        
    def getMenuItem(self,id):
        menu = None
        menu = self.query(Item).filter(Item.id == id).first()
        if menu is None:
            return ({'respCode' : 404})
        else :
            return self.makeItemBean(dict(id = menu.id, name = menu.name, thumbnail = menu.thumbnail, price = menu.price))
            
    def getCatItem(self,id):
        cat = None
        cat = self.query(Category).filter(Category.id == id).first()
        if cat is None:
            return ({'respCode' : 404})
        else :
            return self.makeCategoryBean(dict(id = cat.id, name = cat.name, thumbnail = cat.thumbnail))
            
