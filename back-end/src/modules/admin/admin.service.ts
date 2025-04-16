import { Injectable } from '@nestjs/common';
import { CreateAdminDto } from './dto/create-admin.dto';
import { UpdateAdminDto } from './dto/update-admin.dto';
import { PrismaService } from '../prisma/prisma.service';
import { roles } from '../../configs/config.json';
@Injectable()
export class AdminService {
  constructor(private readonly prisma: PrismaService){}

  public async createAdmin(){
    
  }
}
