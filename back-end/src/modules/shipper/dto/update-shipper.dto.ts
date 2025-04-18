
import { IsNumber, IsString } from "class-validator";
export class UpdateShipperDto{
    @IsString()
    shipper_name?: string;

    @IsString()
    phone?: string;

    @IsNumber()
    deliveredOrders?: number;

    @IsNumber()
    totalEarnings?:number;
}