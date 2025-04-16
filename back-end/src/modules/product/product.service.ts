import { Injectable } from '@nestjs/common';
import { CreateProductDto } from './dto/create-product.dto';
import { UpdateProductDto } from './dto/update-product.dto';
import { PrismaService } from '../prisma/prisma.service';
@Injectable()
export class ProductService {
  constructor(private readonly prisma: PrismaService) {}
  createProduct(createProductDto: CreateProductDto) {
    return this.prisma.product.create({
      data: createProductDto,
    });
  }

  findAllProduct() {
    return this.prisma.product.findMany({
      include: { categories: true },
    });
  }

  findOneProduct(id: number) {
    return this.prisma.product.findUnique({
      where: { id },
      include: { categories: true },
    });
  }

  updateProduct(id: number, updateProductDto: UpdateProductDto) {
    return this.prisma.product.update({
      where: { id },
      data: updateProductDto,
    });
  }
}
