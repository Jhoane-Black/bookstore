CREATE OR REPLACE FUNCTION biauthor() RETURNS trigger AS 
$$
    begin
         if(new.aut_id='')then
          raise exception 'El codigo de el autor no puede estar vacio';
         end if;

         if(new.aut_name='')then
          raise exception 'El autor no es valido';
         end if;

         if exists(select * from webapp_author where aut_name=new.aut_name)then
             raise exception 'El autor ya se encuentra registrado';
         end if;
		 return new;
    end;
  $$
  LANGUAGE 'plpgsql'; 

CREATE TRIGGER tg_author
  BEFORE INSERT OR UPDATE
  ON webapp_author
  FOR EACH ROW
  EXECUTE PROCEDURE biauthor();
  
--antes de insertar un genero
CREATE OR REPLACE FUNCTION bigenere() RETURNS trigger AS 
$$
    begin
         if(new.gen_id='')then
          raise exception 'El codigo de el genero no puede estar vacio';
         end if;

         if(new.gen_name='')then
          raise exception 'El genero no es valido';
         end if;

         if (select EXISTS(select * from webapp_genere where gen_name=new.gen_name))then
             raise exception 'El genero ya se encuentra registrado';
         end if;
		 return new;
    end;
  $$
  LANGUAGE 'plpgsql'; 
insert into webapp_genere values('1','terror')
CREATE TRIGGER tg_genere
  BEFORE INSERT OR UPDATE
  ON webapp_genere
  FOR EACH ROW
  EXECUTE PROCEDURE bigenere();
  
 --antes de insertar un libro
CREATE OR REPLACE FUNCTION bibook() RETURNS trigger AS 
$$
    begin
         if(new.book_id='')then
          raise exception 'El codigo de el libro no puede estar vacio';
         end if;

         if(new.book_title='')then
          raise exception 'El libro no es valido';
         end if;
         return new;
    end;
  $$
  LANGUAGE 'plpgsql'; 
  
 CREATE TRIGGER tg_book
  BEFORE INSERT OR UPDATE
  ON webapp_book
  FOR EACH ROW
  EXECUTE PROCEDURE bibook();

  Drop trigger tg_book on book; -- elimina el disparador tg_book
--

CREATE OR REPLACE FUNCTION ai_bookm()RETURNS trigger AS 
$$    
    begin 
         IF(TG_OP='INSERT')THEN
            update webapp_book set book_price_dis=book_price-(book_price*0.2) where book_price>200000;
         end if;
         RETURN NEW;
     end;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER tgm_book
  AFTER INSERT OR UPDATE
  ON webapp_book
  FOR EACH ROW
  EXECUTE PROCEDURE ai_bookm();
--

INSERT INTO webapp_book
VALUES ('11','Harry Potter Y El Caliz de Fuego','Salamandra','Harry Potter',100,2);

INSERT INTO webapp_book
VALUES ('9','Harry Potter Y La Camara Secreta','Salamandra','Harry Potter',20,20);

INSERT INTO webapp_book (book_id,book_title,book_editorial,book_saga,book_price)
VALUES ('8','Harry Potter Y La Piedra Filosofal','Salamandra','Harry Potter',199000,199000);

select * from webapp_author


CREATE OR REPLACE FUNCTION ai_auth_user() RETURNS TRIGGER AS
$$
	BEGIN
		insert into webapp_client(cli_id, cli_email) values (new.id, new.email);
	RETURN NEW;
	END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER addclient
  BEFORE INSERT
  ON auth_user
  FOR EACH ROW
  EXECUTE PROCEDURE ai_auth_user();