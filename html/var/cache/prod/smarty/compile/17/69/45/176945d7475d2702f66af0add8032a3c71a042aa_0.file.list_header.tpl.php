<?php
/* Smarty version 3.1.34-dev-7, created on 2021-02-05 20:13:35
  from '/var/www/html/admin-daniel/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.34-dev-7',
  'unifunc' => 'content_601d98df4037d6_56290415',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '176945d7475d2702f66af0add8032a3c71a042aa' => 
    array (
      0 => '/var/www/html/admin-daniel/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl',
      1 => 1611237233,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_601d98df4037d6_56290415 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_1746362603601d98df402543_11498928', 'leadin');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, "helpers/list/list_header.tpl");
}
/* {block 'leadin'} */
class Block_1746362603601d98df402543_11498928 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'leadin' => 
  array (
    0 => 'Block_1746362603601d98df402543_11498928',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

	<?php echo '<script'; ?>
 type="text/javascript">
		$(document).ready(function() {
			$(location.hash).click();
		});
	<?php echo '</script'; ?>
>
<?php
}
}
/* {/block 'leadin'} */
}
