import { IsEmail, IsNotEmpty, IsString } from "class-validator";

export class CreateAccountDto {

    @IsNotEmpty()
    @IsString()
    id: string;

    @IsNotEmpty()
    @IsString()
    password: string;

    @IsNotEmpty()
    @IsString()
    role_id: string;
    

}
