import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { ShiperService } from './shiper.service';
import { CreateShiperDto } from './dto/create-shiper.dto';
import { UpdateShiperDto } from './dto/update-shiper.dto';
import { UpdateAccountDto } from '../account/dto/update-account.dto';

@Controller('shipper')
export class ShiperController {
  constructor(private readonly shipperService: ShiperService) {}

  @Post()
  createShipper(@Body() createShiperDto: CreateShiperDto) {
    return this.shipperService.createShiper(createShiperDto);
  }

  @Get(":id")
  getShipperById(@Param("id") id:string){
    return this.shipperService.getShipperById(id);
  }

  @Get()
  getAllShipper(){
    return this.shipperService.getAllShipper();
  }

  @Patch(":id")
  updateShipper(@Param("id") id: string,@Body() data: UpdateShiperDto){
    return this.shipperService.uppdateShipper(id, data);
  }

  @Delete(":id")
  deleteShipper(@Param("id") id: string){
    return this.shipperService.deleteShipper(id);
  }
  
}
