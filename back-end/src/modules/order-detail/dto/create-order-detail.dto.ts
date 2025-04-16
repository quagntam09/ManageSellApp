import { IsNotEmpty, IsNumber, IsString } from "class-validator";

export class CreateOrderDetailDto {
    @IsString()
    @IsNotEmpty()
    OrderId: string;

    @IsString()
    @IsNotEmpty()
    ProductId: string;

    @IsNumber()
    @IsNotEmpty()
    Quantity: number;

}
