import { BadRequestException, Injectable } from '@nestjs/common';
import { CreateAccountDto } from './dto/create-account.dto';
import { PrismaService } from '../prisma/prisma.service';
import * as bcrypt from 'bcryptjs'; // Thêm thư viện bcrypt để mã hóa mật khẩu
@Injectable()
export class AccountService {
  constructor(
    private readonly prisma: PrismaService
  ){}
  public async createAccount(data: CreateAccountDto, password: string) {
    const { admin_id, user_id, role_id } = data;
  
    // Kiểm tra xem có thiếu cả admin_id và user_id không
    if (!admin_id && !user_id) {
      throw new BadRequestException("Thiếu 1 trong 2 Id của admin hoặc user");
    }
  
    // Kiểm tra sự tồn tại của role
    const role = await this.prisma.role.findUnique({ where: { id: role_id } });
    if (!role) {
      throw new BadRequestException("Không tìm thấy role Id");
    }
  
    // Kiểm tra xem tài khoản admin_id hoặc user_id đã tồn tại chưa
    const existingAccount = await this.prisma.account.findFirst({
      where: {
        OR: [
          { admin_id },
          { user_id }
        ]
      }
    });
  
    if (existingAccount) {
      throw new BadRequestException("Tài khoản với admin_id hoặc user_id đã tồn tại");
    }
  
    // Mã hóa mật khẩu
    const hashedPassword = await bcrypt.hash(password, 10);
  
    // Tạo tài khoản mới
    const newAccount = await this.prisma.account.create({
      data: {
        password: hashedPassword,
        admin_id,
        user_id,
        roleId: role_id
      }
    });
  
    return newAccount;
  }
}
