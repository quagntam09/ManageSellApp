import { BadRequestException, Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { UpdateUserDto } from './dto/update-user.dto';
@Injectable()
export class UserService {
  constructor(private readonly prisma: PrismaService,
  ) {}


  public async getAllUser(){
    return this.prisma.user.findMany()
  }

  public async getUserById(id: string){
    return this.prisma.user.findUnique({where: {id}});
  }

  public async updateUser(id: string, data: UpdateUserDto) {
    // Kiểm tra nếu data không có nội dung
    if (!data || Object.keys(data).length === 0) {
      throw new BadRequestException('Không có dữ liệu để cập nhật');
    }
  
    // Cập nhật người dùng với dữ liệu truyền vào
    return this.prisma.user.update({
      where: {
        id: id,  // Sử dụng id từ tham số
      },
      data: {
        ...data,  // Truyền các trường cần cập nhật từ data
      },
    });
  }
  async deleteUser(id: string){
    return this.prisma.user.delete({where: {id}})
  }
}
