import { Injectable } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { UpdateUserDto } from './dto/update-user.dto';
import { PrismaService } from '../prisma/prisma.service';
@Injectable()
export class UserService {
  constructor(private readonly prisma: PrismaService) {}
    createUser(createUserDto: CreateUserDto) {
      return this.prisma.user.create({
        data: createUserDto,
      });
    }
  
    findAllUser() {
      return this.prisma.user.findMany({
        include: { posts: true },
      });
    }
  
    findOneUser(id: number) {
      return this.prisma.user.findUnique({
        where: { id },
        include: { posts: true },
      });
    }
}
