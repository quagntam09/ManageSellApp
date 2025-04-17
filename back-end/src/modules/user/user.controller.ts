import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}
  @Post()
  createUser(@Body() data: CreateUserDto){
    return this.userService.createUser(data)
  }
  @Get()
  getAllUser(){
    return this.userService.getAllUser();
  }

  @Get(":id")
  getUserById(@Param("id") id: string){
    return this.userService.getUserById(id);
  }


  @Patch(":id")
  updateUser(@Param("id") id: string, data: CreateUserDto){
    return this.userService.updateUser(id,data);
  }
}
