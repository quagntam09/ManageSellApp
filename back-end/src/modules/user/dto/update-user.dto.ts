import { IsString, IsOptional, IsNumber, IsNumberString } from "class-validator";
import { Type } from "class-transformer";

export class UpdateUserDto {
  @IsOptional()
  @IsString()
  user_name?: string;

  @IsOptional()
  @IsNumberString()
  phone?: string;

  @IsOptional()
  @Type(() => Number)
  @IsNumber()
  vip?: number;
}
