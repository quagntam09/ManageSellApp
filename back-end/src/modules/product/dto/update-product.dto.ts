import { PartialType } from '@nestjs/mapped-types';
import { CreateProductDto } from './create-product.dto';
import { IsString, IsUUID, IsNumber } from 'class-validator';
export class UpdateProductDto{
        @IsUUID()
        id: string;

        @IsString()
        name: string;
    
        @IsString()
        description: string;
    
        @IsString()
        category: string;
        
        @IsNumber()
        price: number;
    
        @IsNumber()
        stock: number;
}
