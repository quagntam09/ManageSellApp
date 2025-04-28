import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { AccountService } from './account.service';
import { CreateAccountDto } from './dto/create-account.dto';
import { UpdateAccountDto } from './dto/update-account.dto';

@Controller('account')
export class AccountController {
  constructor(private readonly accountService: AccountService) {}
  @Post()
  createAccount(@Body() data: CreateAccountDto){
    return this.accountService.createAccount(data);
  }

  @Get(":id")
  getAccountById(@Param("id") id: string){
    return this.accountService.getAccountById(id);
  }

  @Get()
  getAllAccounts(){
    return this.accountService.getAllAccounts();
  }
}
