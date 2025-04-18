import { IsNotEmpty, IsNumber, IsString } from "class-validator";

export class CreateShipperDto {
    @IsString()
    @IsNotEmpty()
    id: string;

    @IsString()
    @IsNotEmpty()
    shipper_name: string;

    @IsNumber()
    @IsNotEmpty()
    phone: string;

    @IsString()
    @IsNotEmpty()
    password: string;
}
