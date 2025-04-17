import { Module } from '@nestjs/common';
import { ShiperService } from './shiper.service';
import { ShiperController } from './shiper.controller';
import { PrismaService } from '../prisma/prisma.service';
import { AccountService } from '../account/account.service';

@Module({
  controllers: [ShiperController],
  providers: [ShiperService, PrismaService, AccountService],
})
export class ShiperModule {}
