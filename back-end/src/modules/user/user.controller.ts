import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  getAllUser(){
    return this.userService.getAllUser();
  }


  @Patch(":id")
  updateUser(@Param("id") id: string,@Body() data: UpdateUserDto){
    return this.userService.updateUser(id,data);
  }

  @Delete(":id")
  deleteUser(@Param("id") id:string){
    return this.userService.deleteUser(id)
  }
  @Get(":accountId")
  getUserByAccountId(@Param("accountId") accountId: string){
    return this.userService.getUserByAccountId(accountId)
  }

}
