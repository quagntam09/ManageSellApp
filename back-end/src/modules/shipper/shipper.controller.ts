import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { ShipperService } from './shipper.service';
import { CreateShipperDto } from './dto/create-shipper.dto';
import { UpdateShipperDto } from './dto/update-shipper.dto';
import { UpdateAccountDto } from '../account/dto/update-account.dto';

@Controller('shipper')
export class ShipperController {
  constructor(private readonly shipperService: ShipperService) {}


  @Get(":id")
  getShipperById(@Param("id") id:string){
    return this.shipperService.getShipperById(id);
  }

  @Get()
  getAllShipper(){
    return this.shipperService.getAllShipper();
  }

  @Patch(":id")
  updateShipper(@Param("id") id: string,@Body() data: UpdateShipperDto){
    return this.shipperService.uppdateShipper(id, data);
  }

  @Delete(":id")
  deleteShipper(@Param("id") id: string){
    return this.shipperService.deleteShipper(id);
  }
  
}
