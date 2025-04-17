
import { IsNumber, IsString } from "class-validator";
export class UpdateShiperDto{
    @IsString()
    shipper_name?: string;

    @IsString()
    phone?: string;

    @IsNumber()
    deliveredOrders?: number;

    @IsNumber()
    totalEarnings?:number;
}