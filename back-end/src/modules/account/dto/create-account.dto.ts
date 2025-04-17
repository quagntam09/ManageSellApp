import { IsNotEmpty, IsNumber, IsString } from "class-validator";

export class CreateAccountDto {
    @IsString()
    admin_id: string | null;

    @IsString()
    user_id: string | null;

    @IsString()
    shiper_id: string | null;

    @IsNotEmpty()
    @IsNumber()
    role_id: number;
}
