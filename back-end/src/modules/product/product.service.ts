import { Injectable } from '@nestjs/common';
import { CreateProductDto } from './dto/create-product.dto';
import { PrismaService } from '../prisma/prisma.service';
import { UpdateProductDto } from './dto/update-product.dto';
@Injectable()
export class ProductService {
  constructor(private readonly prisma: PrismaService) {}
  createProduct(createProductDto: CreateProductDto) {
    return this.prisma.product.create({
      data: createProductDto,
    });
  }

  deleteProduct(id: string){
    return this.prisma.product.delete({where: {id}})
  }

  getAllProduct(){
    return this.prisma.product.findMany();
  }

  getProductById(id: string){
    return this.prisma.product.findUnique({where: {id}})
  }
}