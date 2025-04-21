import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { ProductService } from './product.service';
import { CreateProductDto } from './dto/create-product.dto';
import { UpdateProductDto } from './dto/update-product.dto';

@Controller('product')
export class ProductController {
  constructor(private readonly productService: ProductService) {}
  @Post()
  creatProduct(@Body() data: CreateProductDto){
    return this.productService.createProduct(data);
  }

  @Patch()
  updateProduct(@Body() data:UpdateProductDto[]){
    return this.productService.updateProduct(data);
  }


  @Delete(":id")
  deleteProduct(@Param("id") id: string){
    return this.productService.deleteProduct(id);
  }

  @Get()
  getAllProduct(){
    return this.productService.getAllProduct();
  }

  @Get(":id")
  getProductById(@Param("id") id: string){
    return this.productService.getProductById(id)
  }
}
