import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';

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
  updateUser(@Param("id") id: string,@Body() data: UpdateUserDto){
    return this.userService.updateUser(id,data);
  }

  @Delete(":id")
  deleteUser(@Param("id") id:string){
    return this.userService.deleteUser(id)
  }
}
