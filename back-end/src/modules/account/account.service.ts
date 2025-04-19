import { BadRequestException, Injectable } from '@nestjs/common';
import { CreateAccountDto } from './dto/create-account.dto';
import { PrismaService } from '../prisma/prisma.service';
import * as bcrypt from 'bcryptjs'; // Thêm thư viện bcrypt để mã hóa mật khẩu
@Injectable()
export class AccountService {
  constructor( 
    private readonly prisma: PrismaService
  ){}
  public async createAccount(data: CreateAccountDto) {
    const { password, role_id, id, phone, name } = data;

    const role = await this.prisma.role.findUnique({ where: { id: role_id } });
    if (!role) {
      throw new BadRequestException("Không tìm thấy role Id");
    }
  
    // Mã hóa mật khẩu
    const hashedPassword = await bcrypt.hash(password, 10);
  
    // Tạo tài khoản mới
    const newAccount = await this.prisma.account.create({
      data: {
        password: hashedPassword,
        roleId: role_id,
        id: id
      }
    });

      switch (role.role_name) {
        case "user":
          await this.prisma.user.create({
            data: {
              user_name: name,   
              phone: phone,     
              account: { connect: { id: newAccount.id } }
            }
          });
          break;
    
        case "shipper":
          await this.prisma.shipper.create({
            data: {
              shipper_name: name, 
              phone: phone,        
              account: { connect: { id: newAccount.id } }
            }
          });
          break;
    
        default:
          throw new BadRequestException("Role chưa được hỗ trợ");
      }
    
      return newAccount;
    }

  async getAccountById(id: string){
    return this.prisma.account.findUnique({where: {id}});
  }
  
}
