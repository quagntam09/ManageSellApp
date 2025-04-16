import { PrismaClient } from '@prisma/client';
import 'dotenv/config';
import { roles, admin } from '../src/configs/config.json';

const prisma = new PrismaClient();

async function main() {
  for (const role of roles) {
    await prisma.role.upsert({
      where: { id: role.role_id },
      update: {},
      create: {
        role_name: role.role_name,
        id: role.role_id
      }
    });
  }
  console.log('Seeded role thành công');

  const adminpass = process.env.ADMIN_PASS;
  if (!adminpass) {
    throw new Error("Thiếu biến môi trường ADDMIN_PASS");
  }

  const adminrole = roles.find((r) => r.role_name === "admin");

  if (adminrole?.role_id) {
    await prisma.admin.upsert({
      where: { id: admin.admin_id },
      update: {},
      create: {
        id: admin.admin_id,
        admin_name: admin.name
      }
    });

    await prisma.account.upsert({
      where: { admin_id: admin.admin_id },
      update: {},
      create: {
        admin_id: admin.admin_id,
        roleId: adminrole.role_id,
        password: adminpass
      }
    });

    console.log('Seeded admin account thành công');
  }
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(() => {
    prisma.$disconnect();
  });
