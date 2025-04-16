import { Module } from '@nestjs/common';
import { UserService } from './user.service';
import { UserController } from './user.controller';
import { PrismaService } from '../prisma/prisma.service';
import { AccountService } from '../account/account.service';

@Module({
  controllers: [UserController],
  providers: [UserService, PrismaService, AccountService],
})
export class UserModule {}
