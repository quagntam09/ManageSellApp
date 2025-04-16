import { IsString, IsNotEmpty, isNotEmpty, IsNumber } from 'class-validator';

export class CreateUserDto {
    @IsString()
    @IsNotEmpty()
    id: string;

    @IsString()
    @IsNotEmpty()
    username: string;

    @IsNumber()
    @IsNotEmpty()
    vip?: number;

    @IsString()
    @IsNotEmpty()
    email: string;

    @IsString()
    @IsNotEmpty()
    password: string;
}
