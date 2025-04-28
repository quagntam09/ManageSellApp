import { BadRequestException, Injectable } from '@nestjs/common';
import { CreateAccountDto } from './dto/create-account.dto';
import { PrismaService } from '../prisma/prisma.service';
import * as bcrypt from 'bcryptjs'; // Thêm thư viện bcrypt để mã hóa mật khẩu
import { link } from 'fs';
@Injectable()
export class AccountService {
  constructor( 
    private readonly prisma: PrismaService
  ){}
  public async createAccount(data: CreateAccountDto) {
    const { password, role_id, id } = data;
  
    // Kiểm tra xem role_id có tồn tại trong cơ sở dữ liệu không
    const role = await this.prisma.role.findUnique({ where: { id: role_id } });
    if (!role) {
      throw new BadRequestException("Không tìm thấy role Id");
    }
  
    // Kiểm tra xem id đã tồn tại trong bảng Account chưa
    const existingAccount = await this.prisma.account.findUnique({
      where: { id: id },
    });
  
    if (existingAccount) {
      throw new BadRequestException("ID đã tồn tại. Vui lòng chọn ID khác.");
    }
  
    // Mã hóa mật khẩu
    const hashedPassword = await bcrypt.hash(password, 10);
  
    // Tạo tài khoản mới
    const newAccount = await this.prisma.account.create({
      data: {
        password: hashedPassword,
        roleId: role_id,
        id: id, // Truyền id được cung cấp
      }
    });
  
    let linkedInfo;
  
    // Tạo thông tin người dùng hoặc shipper tùy theo role
    switch (role.role_name) {
      case "user":
        const userCount = await this.prisma.user.count();
        const newUser = await this.prisma.user.create({
          data: {
            user_name: `user${userCount + 1}`, // user1, user2, user3...
            phone: null,                          // Để trống
            email: null,                          // Để trống
            account: { connect: { id: newAccount.id } }
          }
        });
        linkedInfo = { user: newUser };
        break;  
  
      case "shipper":
        const shipperCount = await this.prisma.shipper.count();
        const newShipper = await this.prisma.shipper.create({
          data: {
            shipper_name: `shipper${shipperCount + 1}`, // shipper1, shipper2...
            phone: null,                                  // Để trống
            email: null,                                  // Để trống
            account: { connect: { id: newAccount.id } }
          }
        });
        linkedInfo = { shipper: newShipper };
        break;
  
      default:
        throw new BadRequestException("Role chưa được hỗ trợ");
    }
  
    return { newAccount, ...linkedInfo };
  }
  
  async getAccountById(id: string){
    return this.prisma.account.findUnique({where: {id}});
  }
  
}
