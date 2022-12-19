#!/usr/bin/env python
# coding: utf-8

# In[19]:


class base:
   
    def length(self):
        return self.l
   
    def breadth(self):
        return self.b
    
   
    def height(self):
        return self.h
    
    
class cuboid(base):
    def volume(self):
        print("volume of cuboid", self.l*self.b*self.h)
    def area(self):
        print("Area of Cuboid",2*((self.l*self.b)+(self.b*self.h)+(self.h*self.l)))
        
        
obj= cuboid()
obj.l = int(input("enter length:"))
obj.b = int(input("enter the breadth"))
obj.h = int(input("enter the height"))

obj.volume()
obj.area()


# In[20]:


#overiding


class a:
    def name(self):
        print("hey i am parent")
class b(a):
    def name(self):
        print("hey i am child")
obj101=b()
obj101.name()


# In[28]:


#overloading


class pest:
    b = 10
    c = 2
    def rect(self,a=20,b=5,c=5):
        
        print("function 1:",a*b*c)
    def rect(self,a=20):
        
        print("function 2:",a)
        
obj1 = pest()
obj1.rect()


# In[29]:


class area:
    def lenbre(self):
        self.l
        self.b
class childd(area):
    def view(self):
        return self.l*self.b
    
obj112 = childd()
obj112.l = 5
obj112.b= 6
obj112.view()


# In[31]:


class values1:
    def get_values(self):
        self.l
        self.b
        
class rect (values1):
    def areaofrect(self):
        print("area of rectangle:" ,self.l*self.b)
        
obj101 = rect()

obj101.l = 20
obj101.b = 10
obj101.areaofrect()


# In[ ]:




