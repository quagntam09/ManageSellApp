import { IsString, IsNotEmpty, IsNumber, IsArray, ValidateNested } from 'class-validator';
import { Type } from 'class-transformer';

class ProductDto {
  @IsString()
  @IsNotEmpty()
  productId: string;

  @IsNumber()
  @IsNotEmpty()
  quantity: number;
}

export class CreateOrderDto {
  @IsString()
  @IsNotEmpty()
  userId: string;

  @IsString()
  @IsNotEmpty()
  address: string;

  @IsNumber()
  @IsNotEmpty()
  totalPrice: number;

  @IsNumber()
  @IsNotEmpty()
  shippingFee: number;

  @IsArray()
  @ValidateNested({ each: true })
  @Type(() => ProductDto)  // Chuyển đổi từng phần tử của mảng thành kiểu ProductDto
  products: ProductDto[];
}
