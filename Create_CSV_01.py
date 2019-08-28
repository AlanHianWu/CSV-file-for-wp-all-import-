#!/usr/bin/env python
import sys

class Line:
    def __init__(self,
                 Sku=None, 
                 Barcode=None, 
                 Image_file_name=None, 
                 Title=None, 
                 Variable=None, 
                 Variable_Name_01=None, 
                 Variable_Value_01=None, 
                 Variable_Name_02=None, 
                 Variable_Value_02=None, 
                 Description_01=None, 
                 Description_02=None, 
                 Price=None, 
                 Price_Exclude_VAT=None, 
                 Brand=None, 
                 Category=None,
                 Images=None):

        self.Sku = Sku
        self.Barcode = Barcode
        self.Image_file_name = Image_file_name
        self.Title = Title
        self.Variable = Variable
        self.Variable_Name_01 = Variable_Name_01
        self.Variable_Value_01 = Variable_Value_01
        self.Variable_Name_02 = Variable_Name_02
        self.Variable_Value_02 = Variable_Value_02
        self.Description_01 = Description_01
        self.Description_02 = Description_02
        self.Images = Images
        self.Price = Price
        self.Price_Exclude_VAT = Price_Exclude_VAT
        self.Brand = Brand
        self.Category = Category
