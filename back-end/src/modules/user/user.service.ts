import { BadRequestException, Injectable } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { PrismaService } from '../prisma/prisma.service';
import {roles} from '../../configs/config.json'
import { AccountService } from '../account/account.service';
import { CreateAccountDto } from '../account/dto/create-account.dto';
@Injectable()
export class UserService {
  constructor(private readonly prisma: PrismaService,
    private readonly accountService: AccountService
  ) {}
  public async createUser(data: CreateUserDto){
    const {password, id, ...res} = data;

    const userrole = roles.find((r) => r.role_name === "user");
    if(!userrole){
      throw new BadRequestException("Không tìm thấy role user");
    }

    const accountData: CreateAccountDto = {
      admin_id: null,
      user_id: id,
      role_id: userrole.role_id
    }

    await this.prisma.user.create({
      data: {
        id: id,
        user_name: data.username,
        vip: Number(data.vip),
        email: data.email
      }
    });

    await this.accountService.createAccount(accountData,password)
    return {
      message: 'Tạo user và account thành công',
      user_id: id
    }
  }

  public async getAllUser(){
    return this.prisma.user.findMany()
  }

  public async getUserById(id: string){
    return this.prisma.user.findUnique({where: {id}});
  }

  public async updateUser(id: string, data: CreateUserDto){
    return this.prisma.user.update({where: {id}, data});
  }
}
