import { Module } from '@nestjs/common';
import { ShipperService } from './shipper.service';
import { ShipperController } from './shipper.controller';
import { AccountService } from '../account/account.service';
import { PrismaService } from '../prisma/prisma.service';

@Module({
  controllers: [ShipperController],
  providers: [ShipperService, AccountService, PrismaService],
})
export class ShipperModule {}
