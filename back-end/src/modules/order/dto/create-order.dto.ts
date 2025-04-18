import { IsNotEmpty, IsNumber, IsString } from "class-validator";

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

    @IsNotEmpty()
    @IsNumber()
    shippingFee: number;

    @IsNotEmpty()
    products:{
        productId: string;
        quantity: number;
    }[];
    
}
