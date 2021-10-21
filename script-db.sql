/*==============================================================*/
/* Table: ROL                                                   */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_ROL INCREMENT BY 1 START WITH 1;
create table ROL (
   ROL_ID               number(10)            not null,
   NOMBRE               varchar2(50)          not null,
   constraint PK_ROL primary key (ROL_ID)
);


/*==============================================================*/
/* Table: OPERACION                                             */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_OPERACION INCREMENT BY 1 START WITH 1;
create table OPERACION (
   OPERACION_ID         number(10)            not null,
   NOMBRE               varchar2(50)          not null,
   constraint PK_OPERACION primary key (OPERACION_ID)
);


/*==============================================================*/
/* Table: ROL_ACCESO                                            */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_ROL_ACCESO INCREMENT BY 1 START WITH 1;
create table ROL_ACCESO (
   ACCESO_ID            number(10)            not null,
   ROL_ID               number(10),
   OPERACION_ID         number(10),
   constraint PK_ROL_ACCESO primary key (ACCESO_ID)
);

alter table ROL_ACCESO
   add constraint FK_ROL_ACCE_REFERENCE_ROL foreign key (ROL_ID)
      references ROL (ROL_ID);

alter table ROL_ACCESO
   add constraint FK_ROL_ACCE_REFERENCE_OPERACIO foreign key (OPERACION_ID)
      references OPERACION (OPERACION_ID);

/*==============================================================*/
/* Table: USUARIO                                               */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_USUARIO INCREMENT BY 1 START WITH 1;
create table USUARIO (
   USUARIO_ID           number(10)            not null,
   NOMBRE               varchar2(25)          not null,
   APELLIDO             varchar2(25)          not null,
   USUARIO              varchar2(15)          not null,
   PASSWORD             varchar2(200)         not null,
   constraint PK_USUARIO primary key (USUARIO_ID)
);

/*==============================================================*/
/* Table: ROL_USUARIO                                           */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_ROL_USUARIO INCREMENT BY 1 START WITH 1;
create table ROL_USUARIO (
   ROL_USUARIO_ID       number(10)            not null,
   USUARIO_ID           number(10),
   ROL_ID               number(10),
   constraint PK_ROL_USUARIO primary key (ROL_USUARIO_ID)
);

alter table ROL_USUARIO
   add constraint FK_ROL_USUA_REFERENCE_USUARIO foreign key (USUARIO_ID)
      references USUARIO (USUARIO_ID);

alter table ROL_USUARIO
   add constraint FK_ROL_USUA_REFERENCE_ROL foreign key (ROL_ID)
      references ROL (ROL_ID);

/*==============================================================*/
/* Table: BITACORA                                              */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_BITACORA INCREMENT BY 1 START WITH 1;
create table BITACORA (
   BIT_ID               number(10)            not null,
   USUARIO_ID           number(10),
   TIPO_MOVIMIENTO      varchar2(10)          not null,
   FECHA                TIMESTAMP             not null,
   TABLA                varchar2(20)          not null,
   REGISTRO_ID          number(10)            not null,
   PADRE_ID             number(10),
   OBJ_OLD              varchar2(2000),
   OBJ_NEW              varchar2(2000),
   constraint PK_BITACORA primary key (BIT_ID)
);

alter table BITACORA
   add constraint FK_BITACORA_REFERENCE_USUARIO foreign key (USUARIO_ID)
      references USUARIO (USUARIO_ID);

/*==============================================================*/
/* Table: ENTIDAD                                               */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_ENTIDAD INCREMENT BY 1 START WITH 1;
create table ENTIDAD (
   ENTIDAD_ID           number(10)            not null,
   NOMBRE               varchar2(50)          not null,
   APELLIDO             varchar2(50)          not null,
   DPI                  varchar2(15),
   NIT                  varchar2(10)          not null,
   TELEFONO             varchar2(8),
   DIRECCION            varchar2(200),
   FECHA_NACIMIENTO     date                  not null,
   CORREO               varchar2(20),
   constraint PK_ENTIDAD primary key (ENTIDAD_ID)
);

/*==============================================================*/
/* Table: EMPLEADO                                              */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_EMPLEADO INCREMENT BY 1 START WITH 1;
create table EMPLEADO (
   EMPLEADO_ID          number(10)            not null,
   JEFE_ID              number(10),
   ENTIDAD_ID           number(10)            not null,
   USUARIO_ID           number(10),
   FECHA_INGRESO        date                  not null,
   FLG_ACTIVO           number(1)             not null,
   constraint PK_EMPLEADO primary key (EMPLEADO_ID)
);

alter table EMPLEADO
   add constraint FK_EMPLEADO_REFERENCE_EMPLEADO foreign key (JEFE_ID)
      references EMPLEADO (EMPLEADO_ID);

alter table EMPLEADO
   add constraint FK_EMPLEADO_REFERENCE_USUARIO foreign key (USUARIO_ID)
      references USUARIO (USUARIO_ID);

alter table EMPLEADO
   add constraint FK_EMPLEADO_REFERENCE_ENTIDAD foreign key (ENTIDAD_ID)
      references ENTIDAD (ENTIDAD_ID);

/*==============================================================*/
/* Table: SUCURSAL                                              */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_SUCURSAL INCREMENT BY 1 START WITH 1;
create table SUCURSAL (
   SUCURSAL_ID          number(10)            not null,
   EMP_ENCARGADO_ID     number(10)            not null,
   DIRECCION            varchar2(100)         not null,
   TELEFONO             varchar2(8)           not null,
   constraint PK_SUCURSAL primary key (SUCURSAL_ID)
);

alter table SUCURSAL
   add constraint FK_SUCURSAL_REFERENCE_EMPLEADO foreign key (EMP_ENCARGADO_ID)
      references EMPLEADO (EMPLEADO_ID);

/*==============================================================*/
/* Table: TURNO                                                 */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_TURNO INCREMENT BY 1 START WITH 1;
create table TURNO (
   TURNO_ID             number(10)            not null,
   SUCURSAL_ID          number(10)            not null,
   EMPLEADO_ID          number(10)            not null,
   FECHA_INICIO         TIMESTAMP             not null,
   FECHA_FIN            timestamp             not null,
   constraint PK_TURNO primary key (TURNO_ID)
);

alter table TURNO
   add constraint FK_TURNO_REFERENCE_SUCURSAL foreign key (SUCURSAL_ID)
      references SUCURSAL (SUCURSAL_ID);

alter table TURNO
   add constraint FK_TURNO_REFERENCE_EMPLEADO foreign key (EMPLEADO_ID)
      references EMPLEADO (EMPLEADO_ID);

/*==============================================================*/
/* Table: PRODUCTO                                              */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_PRODUCTO INCREMENT BY 1 START WITH 1;
create table PRODUCTO (
   PRODUCTO_ID          number(10)            not null,
   NOMBRE               varchar2(50)          not null,
   DESCRIPCION          varchar2(500)         not null,
   COSTO                number(10,2)          not null,
   PRECIO               number(10,2)          not null,
   constraint PK_PRODUCTO primary key (PRODUCTO_ID)
);

/*==============================================================*/
/* Table: INVENTARIO                                            */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_INVENTARIO INCREMENT BY 1 START WITH 1;
create table INVENTARIO (
   INVETARIO_ID         number(10)            not null,
   SUCURSAL_ID          number(10)            not null,
   PRODUCTO_ID          number(10)            not null,
   CANTIDAD             number(10)             not null,
   constraint PK_INVENTARIO primary key (INVETARIO_ID)
);

alter table INVENTARIO
   add constraint FK_INVENTAR_REFERENCE_SUCURSAL foreign key (SUCURSAL_ID)
      references SUCURSAL (SUCURSAL_ID);

alter table INVENTARIO
   add constraint FK_INVENTAR_REFERENCE_PRODUCTO foreign key (PRODUCTO_ID)
      references PRODUCTO (PRODUCTO_ID);

/*==============================================================*/
/* Table: CLIENTE                                               */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_CLIENTE INCREMENT BY 1 START WITH 1;
create table CLIENTE (
   CLIENTE_ID           number(10)            not null,
   ENTIDAD_ID           number(10)            not null,
   PUNTOS               number(10),
   constraint PK_CLIENTE primary key (CLIENTE_ID)
);

alter table CLIENTE
   add constraint FK_CLIENTE_REFERENCE_ENTIDAD foreign key (ENTIDAD_ID)
      references ENTIDAD (ENTIDAD_ID);

/*==============================================================*/
/* Table: ESTADO_VENTA                                          */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_ESTADO_VENTA INCREMENT BY 1 START WITH 1;
create table ESTADO_VENTA (
   ESTADO_VENTA_ID      number(10)            not null,
   DESCRIPCION          varchar2(15)          not null,
   constraint PK_ESTADO_VENTA primary key (ESTADO_VENTA_ID)
);

/*==============================================================*/
/* Table: METODO_PAGO                                           */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_METODO_PAGO INCREMENT BY 1 START WITH 1;
create table METODO_PAGO (
   METODO_PAGO_ID       number(10)            not null,
   DESCRIPCION          varchar2(15)          not null,
   constraint PK_METODO_PAGO primary key (METODO_PAGO_ID)
);

/*==============================================================*/
/* Table: VENTA                                                 */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_VENTA INCREMENT BY 1 START WITH 1;
create table VENTA (
   VENTA_ID             number(10)            not null,
   CLIENTE_ID           number(10),
   EMP_CAJERO_ID        number(10),
   SUCURSAL_ID          number(10),
   METODO_PAGO_ID       number(10),
   ESTADO_VENTA_ID      number(10),
   DOCUMENTO            varchar2(15)          not null,
   FECHA                timestamp             not null,
   DIRECCION_ENTREGA    varchar2(150),
   constraint PK_VENTA primary key (VENTA_ID)
);

alter table VENTA
   add constraint FK_VENTA_REFERENCE_EMPLEADO foreign key (EMP_CAJERO_ID)
      references EMPLEADO (EMPLEADO_ID);

alter table VENTA
   add constraint FK_VENTA_REFERENCE_SUCURSAL foreign key (SUCURSAL_ID)
      references SUCURSAL (SUCURSAL_ID);

alter table VENTA
   add constraint FK_VENTA_REFERENCE_METODO_P foreign key (METODO_PAGO_ID)
      references METODO_PAGO (METODO_PAGO_ID);

alter table VENTA
   add constraint FK_VENTA_REFERENCE_ESTADO_V foreign key (ESTADO_VENTA_ID)
      references ESTADO_VENTA (ESTADO_VENTA_ID);

alter table VENTA
   add constraint FK_VENTA_REFERENCE_CLIENTE foreign key (CLIENTE_ID)
      references CLIENTE (CLIENTE_ID);

/*==============================================================*/
/* Table: DETALLE_VENTA                                         */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_DETALLE_VENTA INCREMENT BY 1 START WITH 1;
create table DETALLE_VENTA (
   DET_VENTA_ID         number(10)            not null,
   VENTA_ID             number(10),
   PRODUCTO_ID          number(10),
   CANTIDAD             number(10)            not null,
   DESCUENTO            number(10,2)          not null,
   PRECIO               number(10,2)          not null,
   constraint PK_DETALLE_VENTA primary key (DET_VENTA_ID)
);

alter table DETALLE_VENTA
   add constraint FK_DETALLE__DET_VENTA_PRODUCTO foreign key (PRODUCTO_ID)
      references PRODUCTO (PRODUCTO_ID);

alter table DETALLE_VENTA
   add constraint FK_DETALLE__REFERENCE_VENTA foreign key (VENTA_ID)
      references VENTA (VENTA_ID);

/*==============================================================*/
/* Table: PROVEEDOR                                             */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_PROVEEDOR INCREMENT BY 1 START WITH 1;
create table PROVEEDOR (
   PROVEEDOR_ID         number(10)            not null,
   ENTIDAD_ID           number(10),
   constraint PK_PROVEEDOR primary key (PROVEEDOR_ID)
);

alter table PROVEEDOR
   add constraint FK_PROVEEDO_REFERENCE_ENTIDAD foreign key (ENTIDAD_ID)
      references ENTIDAD (ENTIDAD_ID);

/*==============================================================*/
/* Table: ESTADO_COMPRA                                         */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_ESTADO_COMPRA INCREMENT BY 1 START WITH 1;
create table ESTADO_COMPRA (
   ESTADO_COMPRA_ID     number(10)            not null,
   DESCRIPCION          varchar2(15)          not null,
   constraint PK_ESTADO_COMPRA primary key (ESTADO_COMPRA_ID)
);

/*==============================================================*/
/* Table: COMPRA                                                */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_COMPRA INCREMENT BY 1 START WITH 1;
create table COMPRA (
   COMPRA_ID            number(10)            not null,
   PROVEEDOR_ID         number(10),
   SUCURSAL_ID          number(10),
   ESTADO_COMPRA_ID     number(10),
   DOCUMENTO            varchar2(15)          not null,
   FECHA                timestamp             not null,
   constraint PK_COMPRA primary key (COMPRA_ID)
);

alter table COMPRA
   add constraint FK_COMPRA_REFERENCE_PROVEEDO foreign key (PROVEEDOR_ID)
      references PROVEEDOR (PROVEEDOR_ID);

alter table COMPRA
   add constraint FK_COMPRA_REFERENCE_SUCURSAL foreign key (SUCURSAL_ID)
      references SUCURSAL (SUCURSAL_ID);

alter table COMPRA
   add constraint FK_COMPRA_REFERENCE_ESTADO_C foreign key (ESTADO_COMPRA_ID)
      references ESTADO_COMPRA (ESTADO_COMPRA_ID);

/*==============================================================*/
/* Table: DETALLE_COMPRA                                        */
/*==============================================================*/
CREATE SEQUENCE SEQ_ID_DETALLE_COMPRA INCREMENT BY 1 START WITH 1;
create table DETALLE_COMPRA (
   DET_COMPRA_ID        number(10)            not null,
   COMPRA_ID            number(10),
   PRODUCTO_ID          number(10),
   CANTIDAD             number(10)            not null,
   DESCUENTO            number(10,2)          not null,
   PRECIO               number(10,2)          not null,
   constraint PK_DETALLE_COMPRA primary key (DET_COMPRA_ID)
);

alter table DETALLE_COMPRA
   add constraint FK_DETALLE__DET_COMPR_PRODUCTO foreign key (PRODUCTO_ID)
      references PRODUCTO (PRODUCTO_ID);

alter table DETALLE_COMPRA
   add constraint FK_DETALLE__REFERENCE_COMPRA foreign key (COMPRA_ID)
      references COMPRA (COMPRA_ID);

