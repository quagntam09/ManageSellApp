import { IsString, IsNotEmpty, IsNumber, IsInt, isNotEmpty } from 'class-validator';

export class CreateProductDto {
    @IsString()
    @IsNotEmpty()
    name: string;

    @IsString()
    @IsNotEmpty()
    description: string;

    @IsString()
    @IsNotEmpty()
    categoryId: string;
    
    @IsNumber()
    @IsNotEmpty()
    price: number;

    @IsInt()
    @IsNotEmpty()
    stock: number;

    @IsNumber()
    @IsNotEmpty()
    rate: number

    img: string;
}
